from optparse import OptionParser
import requests

# Rest endpoint to get the galicaster state
GALICASTER_STATE = "/state"


def get_hostname(options):
    response = get_galicaster_state(options)
    print response['hostname']


def get_profile(options):
    response = get_galicaster_state(options)
    print response['current-profile']


def get_network(options):
    response = get_galicaster_state(options)
    print response['net']


def get_recording_state(options):
    response = get_galicaster_state(options)
    print response['is-recording']


# Actions dict
actions = {"hostname": get_hostname,
           "current_profile": get_profile,
           "network": get_network,
           "is_recording": get_recording_state,
           }


def get_galicaster_state(options):
    url = "http://" + options.host + ":" + options.port
    r = requests.get(url + GALICASTER_STATE)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    response = r.json()
    return response


def warning(options):
    print "Please check %prog --help for the correct syntax"


def process_action(parser, options):
    actions.get(options.action)(options)


def get_config():
    print 'todo'


def main():

    parser = OptionParser(usage="%prog [-c] [-a]", version="%prog 0.1")
    parser.add_option("-a", "--action", dest="action", nargs=1, type="choice",
                        choices=["hostname", "current_profile", "network", "is_recording"],
                        help="Options: hostname, current_profile, network and is_recording.")
    parser.add_option("-c", "--config", dest="config", nargs=1, type="string",
                      help="Provide a config file containing the matterhorn server details, "
                      "this config file can be the galicaster config file. If a separate config "
                      "file is choosen, make sure it's in the ini format and contains the same values "
                      "as the galicaster config file (for opencast connection).")
    parser.add_option("--host", dest="host", default="localhost",
                      help="Ip address for the galicaster agent, default is localhost")
    parser.add_option("-p", "--port", dest="port", default="8080",
                      help="Port for the galicaster rest interface, default is 8080")

    (options, args) = parser.parse_args()

    if not(options.action):
        parser.error("Incorrect number of arguments, please provide an action and config file.")

    process_action(parser, options)


if __name__ == "__main__":
    main()
