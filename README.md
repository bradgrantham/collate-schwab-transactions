Since the beginning of 2018, Schwab doesn't break out positions of a 401K account by fund.  The web site only shows the Schwab portfolio type, e.g. "103".  Schwab does, however, actually buy and sell and collect dividends from individual funds.  They just don't want to bother reporting that on their web page.

This script will collate the result of a complete transaction history for a Schwab 401K account stored in CSV.  You can download that using the "History and Statement" tab.

If you want to track your own account, you'll need to populate the "long_name_to_symbol" and "funds" arrays.  I think it would also be easy to generalize to any list of funds; I just haven't bothered.
