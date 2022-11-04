my_hosts = []
oui_id = {
    "11:22:33": "Dell laptop",
    "44:55:66": "Acer laptop"
}


def remove_brackets(string_with_brackets):
    string_without_brackets = str(string_with_brackets.strip('('))
    string_without_brackets = str(string_without_brackets.strip(')'))
    return string_without_brackets


if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    # Open the logfile for read
    logfilename = "dhcpd.log"
    logfile = open(logfilename, "r")
    # Iterate through every line in the log fil
    for line in logfile:
        # Parse the line type
        interesting_bit = line[34:]
        list_of_values = interesting_bit.split(" ")
        # Handle each line type 
        if list_of_values[0] == "DHCPACK":
            # There are two different formats for the DHCP ACK line
            if list_of_values[1] == "on":
                ipv4 = list_of_values[2]
                mac_address = remove_brackets(list_of_values[4]).upper()
                # Check to see if this host was previously identified
                if mac_address in my_hosts:
                    pass
                else:
                    # Add this new host to the my_hosts list
                    my_hosts.append(mac_address)
                    host_name = remove_brackets(list_of_values[5]).upper()
                    # Some sentences do not have a host name
                    if host_name == "VIA":
                        host_name = "Not present"
                    print(f"ON IP {ipv4} and MAC {mac_address} and my hosname is {host_name}")
            elif list_of_values[1] == "to":
                ipv4 = list_of_values[2]
                mac_address = remove_brackets(list_of_values[3]).upper()
                # Check to see if this host was previously identified
                if mac_address in my_hosts:
                    pass
                else:
                    # Add this new host to the my_hosts list
                    my_hosts.append(mac_address)
                    host_name = remove_brackets(list_of_values[5]).upper()
                print(f"TO IP {ipv4} and MAC {mac_address}")
    print(my_hosts)
    



else:
    print(f"This module is called {__name__} and is being called by another script")