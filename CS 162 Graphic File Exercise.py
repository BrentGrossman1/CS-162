


import matplotlib.pyplot as plot

# set up your lists
numlist = [16, 12, 10, 6]

# noob, experienced, veteran, and master are referencing skill levels
namelist = ['noob', 'experienced', 'veteran', 'master']

colorlist = ['crimson', 'forestgreen', 'magenta', 'gold' ]

explodelist = [0.0, 0.0, 0.2, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%1.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 180, textprops={'fontsize': 14})
plot.axis('equal')

# plot.title() to add my initials, fontsize= to set the characters size, and loc= to place initials on the top left
plot.title('BRG', fontsize = 20, loc= 'left')

plot.savefig('piechart.png')













