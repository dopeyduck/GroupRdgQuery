This file allows the user to query an TEI compliant XML collation file in order to identify readings attested by certain witnesses and not others. There are four inputs:

1. Included witnesses
2. Excluded witnesses
3. The path for the XML file
4. The witness threshold

The script looks for readings attested by some or all of the included witnesses, but not by the excluded witnesses, based on a specified threshold. For example, if the user wants to find all readings attested by at least 20 of 30 included witnesses and not by any of the excluded witnesses, the script will return the variant reading addresses in the Terminal.
