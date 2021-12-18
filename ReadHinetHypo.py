#
# read a htnl file on NIED's Hi-net auto Eq. catalogue 
# and convert Pandas data frame
#
# < Note >
# use Safari or Firefox when downloading the html file on eq. catalogue
# the part of eq. catalogue is missing when using Google Chrome
#
import pandas as pd
from bs4 import BeautifulSoup

###
def ReadHinetHypo(FullPath2File):
    html = open(FullPath2File, 'rt', encoding='euc-jp').read()
    soup = BeautifulSoup(html, 'html.parser')

    pre = soup.pre
    lists = pre.string.get_text().split('\n')
    Hypos = []
    for line in lists[2:-2]:
        tmp = line.split()
        Hypos.append(tmp)
    
# convert list to data frame
    columns = ['Date', 'Time', 'Terr', 'Lat', 'Yerr', 'Lon', 'Xerr', 'Depth', 'Zerr', 'Mag' ]
    HypoDF = pd.DataFrame( Hypos, columns=columns )
    HypoDF[ 'DateTime' ] = pd.to_datetime( HypoDF['Date'].str.cat(HypoDF['Time'], sep=' ') )
    print( HypoDF )

    return HypoDF

#
###
#
def main():
    Fullpath2File = 'Hi-net自動処理震源リスト.html'
    HypoDF = ReadHinetHypo(Fullpath2File)

    return

###
if __name__ == '__main__':
    main()

