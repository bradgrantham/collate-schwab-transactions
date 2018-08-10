import math
import sys
import csv

long_name_to_symbol = {
    "Voya Global Real Estate I" : "IGLIX",
    "American Funds Europacific Growth R5" : "RERFX",
    "Lord Abbett Developing Growth A" : "LAGWX",
    "Metropolitan West Total Return Bd M" : "MWTRX",
    "Vanguard 500 Index Admiral" : "VFIAX",
    "American Century Growth I" : "TWGIX",
    "Schwab Value Advantage Money Ultra": "SNAXX",
    "JPMorgan Mid Cap Value L" : "FLMVX",
    "Metropolitan West Total Return Bd I" : "MWTIX",
    "American Funds AMCAP R4" : "RAFEX",
    "Cash" : "cash",
    "Vanguard Institutional Index I" : "VINIX",
    "American Funds Europacific Growth R6" : "RERGX",
    "Schwab Government Money Inv" : "SNVXX",
    "Pioneer Strategic Income Y" : "STRYX",
    "Invesco Diversified Dividend R5" : "DDFIX",
    "T. Rowe Price QM US Small-Cap Gr Eq I" : "TQAIX",
    "Lord Abbett Developing Growth I" : "LADYX",
    "Oppenheimer International Growth Y" : "OIGYX",
}

headers = sys.stdin.readline()

f = csv.reader(sys.stdin)

# "Transaction Date","Investment","Contribution","Description","Activity","Price","Units","Amount",
# "2/28/2018 12:00:00 AM","Vanguard Institutional Index I","Matching","Contributions - Employer","Purchase","247.900000","0.181000000","44.89",

funds = {
    "IGLIX": 0,
    "RERFX": 0,
    "LAGWX": 0,
    "MWTRX": 0,
    "VFIAX": 0,
    "TWGIX": 0,
    "SNAXX": 0,
    "DDFIX": 0,
    "FLMVX": 0,
    "OIGYX": 0,
    "STRYX": 0,
    "LADYX": 0,
    "RERGX": 0,
    "MWTIX": 0,
    "RAFEX": 0,
    "VINIX": 0,
    "SNVXX": 0,
    "TQAIX": 0,
    "cash": 0,
}

cash = 0

for row in f:
    [date, fund, type, whom, what, price, units, amount] = row[0:8]

    fund = long_name_to_symbol[fund]

    if what == 'Purchase':
        funds[fund] += float(units)
    elif what == 'Transfer In':
        funds[fund] += float(units)
        print "transfer in %f of %s" % (float(amount), fund)
    elif what == 'Sale':
        funds[fund] += float(units)
    elif what == 'Cash Receipts':
        print "cash receipt for %f" % float(amount)
    elif what == 'Cash Disbursement':
        print "cash disbursement for %f" % float(amount)
    else :
        print "'%s'" % what, row
        sys.exit(1)

for (fund, amount) in funds.iteritems():
    if abs(amount) >= 0.00001:
        print "%s, %f" % (fund, amount)
# for (fund, amount) in funds.iteritems():
    # if abs(amount) >= 0.00001:
        # print "%f" % (amount)
