/**
 * \file
 * \brief Start Beagle application
 */
#ifndef BEAGLE_RELAY_APP_HPP
#define BEAGLE_RELAY_APP_HPP

#include "Poco/Util/ServerApplication.h"
#include "Poco/Util/OptionSet.h"


class BeagleRelayApp: public Poco::Util::ServerApplication {
protected:
	void defineOptions(Poco::Util::OptionSet& options) override;

	int main(const Poco::Util::Application::ArgVec& args) override;

    void handlePin(const std::string& name, const std::string& value);

	static void handleSignal(int signum);

public:
    static unsigned long pin;
};

#endif // BEAGLE_RELAY_APP_HPP
