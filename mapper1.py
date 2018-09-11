#!/usr/bin/env python
import sys
for line in sys.stdin:
    # Setting some defaults
	user_id = ""
	product_id = "-"
	location = "-"

	line = line.strip()
	splits = line.split("\t")
	if len(splits) == 5: # Transactions have more columns than users
		user_id = splits[1]
		product_id = splits[2]
	elif len(splits)==3:  #user
		user_id = splits[0]
		location = splits[1]
	else :
		print "aya"
		continue                   
	print '%s\t%s\t%s' % (user_id,product_id,location)
