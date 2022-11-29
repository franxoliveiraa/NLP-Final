import pandas as pd
import re

path = '/Users/gracewagner/Desktop/nlp/project'

### Read metadata into dataframe from excel file
# data = pd.read_excel(r'/Users/gracewagner/Desktop/nlp/project/sources_movies.xlsx', sheet_name='Sheet1')
# df = pd.DataFrame(data, columns=['textID','title','year','country','genre'])
# movie_ids = df['textID'].tolist()
# movie_countries = df['country'].tolist()
# id_to_country = dict(zip(movie_ids, movie_countries))

def get_movies():
    prev_id = 0
    count = 0
    movies = []
    write = True

    with open(path + '/subtitles_en', 'r') as subtitles, open(path + '/subtitles_ids', 'r') as ids, open(path + '/subtitles_data', 'w') as cleaned:
        while True:
            id_line = ids.readline()
            sub_line = subtitles.readline()
            if not (id_line or sub_line):
                break          
            id_fields = id_line.split('/')
            curr_id = int(id_fields[2])
            if curr_id != prev_id:
                prev_id = curr_id
                year = int(id_fields[1])
                if year == 0:
                    write = False
                    continue
                elif curr_id not in movie_ids:
                    write = False
                    continue
                elif "USA" not in str(id_to_country.get(curr_id)):
                    write = False
                    continue
                else:
                    write = True
                    cleaned.write('***'+str(curr_id)+','+str(year)+','+str(count)+'***\n')
                    movies.append(curr_id)
                    if count%100 == 0:
                        print(str(curr_id) + '\n')
                    count += 1           
            if write == True:
                cleaned.write(sub_line)

    print("COUNT: " + str(len(movies)))
    return movies

def get_decades():
    thirties = []
    fourties = []
    fifties = []
    sixties = []
    seventies = []
    eighties = []
    nineties = []
    oughts = []
    tens = []

    with open(path + '/subtitles_data', 'r') as subtitles:
        while True:
            line = subtitles.readline()
            if not line:
                break
            matched = re.match("\*\*\*[0-9]+,[0-9]+,[0-9]+\*\*\*", line)
            is_match = bool(matched)
            if is_match:
                fields = line.strip('*').split(',')
                id = int(fields[0])
                year = int(fields[1])
                if 1930 <= year <= 1939:
                    thirties.append(id)
                elif 1940 <= year <= 1949:
                    fourties.append(id)
                elif 1950 <= year <= 1959:
                    fifties.append(id)
                elif 1960 <= year <= 1969:
                    sixties.append(id)
                elif 1970 <= year <= 1979:
                    seventies.append(id)
                elif 1980 <= year <= 1989:
                    eighties.append(id)
                elif 1990 <= year <= 1999:
                    nineties.append(id)
                elif 2000 <= year <= 2009:
                    oughts.append(id)
                else:
                    tens.append(id)
    
    print("30s: " + str(len(thirties)))
    print("40s: " + str(len(fourties)))
    print("50s: " + str(len(fifties)))
    print("60s: " + str(len(sixties)))
    print("70s: " + str(len(seventies)))
    print("80s: " + str(len(eighties)))
    print("90s: " + str(len(nineties)))
    print("00s: " + str(len(oughts)))
    print("10s: " + str(len(tens)))


# movie_list = get_movies()
get_decades()

            