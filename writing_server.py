from ctypes.wintypes import WORD
import re
from flask import Flask, json, request, jsonify, Response
from textblob import TextBlob
from spellchecker import SpellChecker
#from flask_cors import CORS, cross_origin
app = Flask(_name_)


def preChecks(data):
    
    
    disallwoed_characters ="._!,'"
    #data = data.strip()
    #disallowed_patterns ="b'"
    for c in disallwoed_characters:
        if c == '.':
            data =data.replace(c," ")
        else:
            data = data.replace(c,"")
        data = data.replace('b\'',"")
        
    
    split_Sen = data.split(' ')
    #print(split_Sen) 
    spell = SpellChecker()
    total_word_count = len(list(split_Sen))
    # print(total_word_count)
    split_list= list(spell.unknown(split_Sen))
    # split_list.remove('')
    
    #split_list= [re.sub(r'[^a-zA=Z0-9]','',s) for s in split_list]
    #incorrect_spells = spell.unknown(split_list)
        
    print(split_list)
    count = len(split_list)
    #return str(count)
    # print(count)
    weight_threshold_band = [100,95,85,75,65,55,45,35,25]
    actual_threshold_band = (1-(count/total_word_count))*100
    #print(actual_threshold_band)
    if actual_threshold_band >= weight_threshold_band[0]:
        return "Wrong words are {} and the band is 9".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[1]) and (actual_threshold_band<=weight_threshold_band[0])):
        return "Wrong words are {} and the band is 8".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[2]) and (actual_threshold_band<=weight_threshold_band[1])):
        return "Wrong words are {} and the band is 7".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[3]) and (actual_threshold_band<=weight_threshold_band[2])):
        return "Wrong words are {} and the band is 6".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[4]) and (actual_threshold_band<=weight_threshold_band[3])):
        return "Wrong words are {} and the band is 5".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[5]) and (actual_threshold_band<=weight_threshold_band[4])):
        return "Wrong words are {} and the band is 4".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[6]) and (actual_threshold_band<=weight_threshold_band[5])):
        return "Wrong words are {} and the band is 3".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[7]) and (actual_threshold_band<=weight_threshold_band[6])):
        return "Wrong words are {} and the band is 2".format(split_list)
    elif ((actual_threshold_band >= weight_threshold_band[8]) and (actual_threshold_band<=weight_threshold_band[7])):
        return "Wrong words are {} and the band is 1".format(split_list)
    else:
        return "Wrong words are {} and the band is 0".format(split_list)



@app.route('/writing', methods=['GET','POST'])
#@cross_origin()
def home(): 
    count_misspells=""
    if request.method == 'POST':
        data = json.loads(request.data)
        data1 = str(data['data'])
        # print(data1)
        count_misspells = preChecks(data1)
    return str(count_misspells)

    
if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5002)