# Log Hunt

Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?
Download the logs and figure out the full flag from the fragments.

## Background

This Challenge had a downloadable Log File along with two Hints:

1] You can use grep to filter only matching lines from the log.
2] Some lines are duplicates; ignore extra occurrences.

It was classified under "General Skills", and therefore it meant that it required you to apply a variety of competencies to retrieve The Flag...

## Procedure

**Step #1:** This was relatively straightforward, even without the Hints. First, download and open the Log File...

**Step #2:** Next, look through the Log Entries and notice how the first one has what looks like the first part of The Flag. This means that similar to the Hint, we need to filter similar Entries. One way is to use `grep 'FLAGPART' server.log | sort | uniq`. Note that you can use whichever variation suits your best and this is not the exhaustive Command...

**Step #3:** The Output will consist of repeated Log Entries. Our Command did not completely filter them since while their Values are the same, the Timestamps are still unique, and therefore the Log Entries are each treated as unique. Take note of the pattern to pick The Flag's components and assemble them. There you go...


## Conclusion

This Task simply tested your ability to look for Patterns and obviously Linux as part of the General Skills needed in Cyber Security...
