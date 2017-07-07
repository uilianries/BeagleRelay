#include "app.hpp"

#include <csignal>
#include <thread>
#include <chrono>

#include <Poco/Util/Option.h>
#include <Poco/Util/IntValidator.h>
#include <Poco/Util/OptionCallback.h>

#include "bbbgpio/stream.hpp"

unsigned long BeagleRelayApp::pin = 60;

void BeagleRelayApp::defineOptions(Poco::Util::OptionSet& options) {
    ServerApplication::defineOptions(options);

	options.addOption(
            Poco::Util::Option("pin", "p", "GPIO Pin (default: 60)")
        				.required(false)
        				.repeatable(false)
                        .validator(new Poco::Util::IntValidator(0, 100))
        				.callback(Poco::Util::OptionCallback<BeagleRelayApp>(this, &BeagleRelayApp::handlePin)));
}

void BeagleRelayApp::handlePin(const std::string& name, const std::string& value) {
    BeagleRelayApp::pin = std::stol(value);
}



void BeagleRelayApp::handleSignal(int signum) {
    bbb::gpio::logic_ostream ogpio(BeagleRelayApp::pin);

    ogpio << bbb::gpio::pin_level::high;
    std::this_thread::sleep_for(std::chrono::seconds(1));
    ogpio << bbb::gpio::pin_level::low;
}

int BeagleRelayApp::main(const Poco::Util::Application::ArgVec& args) {
    signal(SIGUSR1, &BeagleRelayApp::handleSignal);
    waitForTerminationRequest();
    return Poco::Util::Application::EXIT_OK;
}
