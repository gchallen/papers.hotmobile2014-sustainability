#!/usr/bin/env python

import sys,csv,re

applicationSupporters = []
infrastructureSupporters = []
networkingSupporters = []
systemsSupporters = []

supportReader = csv.DictReader(open(sys.argv[1]))
applicationOutfile = open("applicationsupporters.tex", "w")
infrastructureOutfile = open("infrastructuresupporters.tex", "w")
networkingOutfile = open("networkingsupporters.tex", "w")
systemsOutfile = open("systemssupporters.tex", "w")

for row in supportReader:
  if row['Primary Interest'] == None or row['Primary Interest'] == '':
    continue
  if row['I/E'] == 'I':
    continue
  if re.match("A", row['Primary Interest']):
    applicationSupporters.append(row)
  elif re.match("I", row['Primary Interest']):
    infrastructureSupporters.append(row)
  elif re.match("N", row['Primary Interest']):
    networkingSupporters.append(row)
  elif re.match("O", row['Primary Interest']):
    systemsSupporters.append(row)

applicationSupporters.sort(key=lambda supporter: supporter['Last Name'])
infrastructureSupporters.sort(key=lambda supporter: supporter['Last Name'])
networkingSupporters.sort(key=lambda supporter: supporter['Last Name'])
systemsSupporters.sort(key=lambda supporter: supporter['Last Name'])

preface = "\\item \\textbf{Interested Researchers ---}"
print >>applicationOutfile, "%s %s." % (preface, ", ".join([("%s (%s)" % (i['Name'], i['Affiliation'])) for i in applicationSupporters]))
print >>infrastructureOutfile, "%s %s." % (preface, ", ".join([("%s (%s)" % (i['Name'], i['Affiliation'])) for i in infrastructureSupporters]))
print >>networkingOutfile, "%s %s." % (preface, ", ".join([("%s (%s)" % (i['Name'], i['Affiliation'])) for i in networkingSupporters]))
print >>systemsOutfile, "%s %s." % (preface, ", ".join([("%s (%s)" % (i['Name'], i['Affiliation'])) for i in systemsSupporters]))
