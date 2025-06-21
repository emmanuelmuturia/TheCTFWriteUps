# Task #21: Read the packet

I just hacked my neighbor's WiFi and try to capture some packet. He must be up to no good. Help me find it.

[Please download the task file[s]...]

## Background

The task file is a Network Capture File, meaning that we need Wireshark to interpret its content...

## Procedure

**Step #1:** Set up Wireshark and open the file...

**Step #2:** In the Filter, type HTTP since the flag is likely found in a HTTP Packet as it has no encryption...

**Step #3:** Scroll through the Packets and notice the one that has the flag.txtlabel in the "Info" column. Notice the "GET". This suggests that a file with that name was retrieved through a HTTP Request...

**Step #4:** Just as The Hint specified, we need to view the entire Stream. Right-click the Packet and select "Follow > HTTP Stream". The flag is in the second-last line...

## Conclusion

This task uniquely tested your Network Traffic Analysis skills. This is essential in roles like SOC Analysis where inspecting Packets is not just foundational but critical. You are now done with CTFs Collection Vol. 1...
