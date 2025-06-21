# Task #7: QRrrrr

Reverse it or read it?

[Please download the task file[s]...]

## Background

We can see that the downloaded task file has a ".hello" extension. What does this mean for us?

## Procedure

**Step #1:** Since you are obviously using Linux, navigate to the file's location using the Terminal...

**Step #2:** For us to know what type of file this is, use the `file [File Name]` command. We will see that the file is a Linux Executable...

**Step #3:** Let us execute the file by first assigning it Execute Permissions using the `chmod +x [File Name]` command...

**Step #4:** We will execute it by typing: `./[File Name]` and hitting ENTER. It will print the message, "Hello there, wish you have a nice day". Not wuite helpful, is it?

**Step #5:** Since this is a Raw Executable kind of file, it also means that we can read its contents, similar to what the task's title hints at. In Linux, this is quite easy since we can use the `strings` command to read any HUman-readable content in the file. Use the `strings [File Name]` command to do so and when you scroll through the printed content, you will eventually find the flag. An easier way to do it would be by filtering the output like this: `strings [File Name] | grep 'THM'`...

## Conclusion

This task tested our Binary File Inspection and Reverse Engineering skills. These are quite essential in Cyber Security and it only gets better from here. Task #8 is calling...
