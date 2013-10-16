#!/usr/bin/env python

import sys,csv,re

externalSupporters = []
internalSupporters = []

supportReader = csv.DictReader(open(sys.argv[1]))
outfile = open('supporttable.tex', 'w')

for row in supportReader:
  if row['Primary Interest'] == None or row['Primary Interest'] == '':
    continue
  if row['I/E'] == 'I':
    internalSupporters.append(row)
  else:
    externalSupporters.append(row)

internalSupporters.sort(key=lambda supporter: supporter['Last Name'])
externalSupporters.sort(key=lambda supporter: supporter['Last Name'])

count = 1
for i, supporter in enumerate(externalSupporters):
  supporter['Index'] = count + i
count = i + 2
for i, supporter in enumerate(internalSupporters):
  supporter['Index'] = count + i

print >>outfile,'''\
% 31 Oct 2010 : GWA : THIS FILE IS AUTOGENERATED. DO NOT EDIT.
%               Please edit ./figures/gensupporttable.py instead.'''

print >>outfile,r'''
{\small \begin{tabularx}{\textwidth}{rXrX}
\multicolumn{4}{c}{\large{\textbf{\PhoneLab{} Supporters}}} \\ \midrule
\multicolumn{2}{c}{\large{\textbf{External}}} &
\multicolumn{2}{c}{\large{\textbf{Internal}}} \\
\cmidrule(lr){1-2} \cmidrule(lr){3-4}'''

for i in range(max([len(externalSupporters), len(internalSupporters)])):
  if i >= len(externalSupporters):
    externalString = " & "
  else:
    externalString = "%d. & %s \\hfill \\emph{%s}" % (externalSupporters[i]['Index'],
                                            externalSupporters[i]['Name'],
                                            externalSupporters[i]['Affiliation'])
    externalName = externalSupporters[i]['Name']
    externalAffiliation = externalSupporters[i]['Affiliation']
  if i >= len(internalSupporters):
    internalString = " & "
  else:
    affiliation = re.sub(r'\s*UB\s*', r'', internalSupporters[i]['Affiliation'])
    internalString = "%d. & %s \\hfill \\emph{%s}" % (internalSupporters[i]['Index'],
                                            internalSupporters[i]['Name'],
                                            affiliation)
  print >>outfile, "%s & %s \\\\" % (externalString, internalString)

print >>outfile,r'''
\end{tabularx}}'''
