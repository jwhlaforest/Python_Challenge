import os
import csv

#file path
csvpath = os.path.join('Resources','election_data.csv')

#opening and reading the election data
with open(csvpath, 'r') as csvfile:
    elec_data = csv.reader(csvfile, delimiter=',')
    next(elec_data)

    #variables
    votes = 0
    cand = ''
    cand_votes = {}
    cand_perc = {}
    win_votes = 0
    winner = ''

    #vote and vote per candidate counter
    for line in elec_data:
        votes = votes + 1
        cand = line[2]
        if cand in cand_votes:
            cand_votes[cand] = cand_votes[cand] + 1
        else:
            cand_votes[cand] = 1

#percentage calculation
for person, vote_count in cand_votes.items():
    cand_perc[person] = '{0:.3%}'.format(vote_count / votes)
    if vote_count > win_votes:
        win_votes = vote_count
        winner = person

print('Election Results')
print('-------------------------')
print('Total Votes:',votes)
print('-------------------------')
for person, vote_count in cand_votes.items():
    print(person,':',cand_perc[person],'(',vote_count,')')
print('-------------------------')
print('Winner:',winner)
print('-------------------------')

with open('PyPoll.txt','w') as f:
    print('Election Results', file = f)
    print('-------------------------', file = f)
    print('Total Votes:',votes, file = f)
    print('-------------------------', file = f)
    for person, vote_count in cand_votes.items():
        print(person,':',cand_perc[person],'(',vote_count,')', file = f)
    print('-------------------------', file = f)
    print('Winner:',winner, file = f)
    print('-------------------------', file = f)