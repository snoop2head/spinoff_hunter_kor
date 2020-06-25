from collections import Counter

from detect_company import yield_frequency_data


def count_spinoffs(companies: list, articles: list) -> dict:
    # sum two dictionaries as Counter Object
    mergedFrequencyData = {}
    sum_freq_counterObj = Counter(mergedFrequencyData)
    for url in articles:
        frequencyData = yield_frequency_data(url, companies)
        freq_counterObj = Counter(frequencyData)
        sum_freq_counterObj = sum_freq_counterObj + freq_counterObj
        print(sum_freq_counterObj)

    # tranform Counter Object into dictionary
    sum_frequency = dict(sum_freq_counterObj)
    print(sum_frequency)
    return sum_frequency


"""
from get_spinoff_info import iterate_avail_articles
from extract_company_list import yield_kospi_companies

spinoff_articles_list = [
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006241133130960107154&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006241132074760108114&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006231009195400102978&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006220912030400103218&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006220946501400103784&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006191422511360102743&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006191355276840108314&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006171057167720103744&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006170857397900106488&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006161007559840103880&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006151219088080103955&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006011346333920106338&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006091111551720101643&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006050007288710109271&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006041639085320105693&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006040805415520108351&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006020839096980103239&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005281313475600109260&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005271450373280108877&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005261431077640106346&lcode=00&page=2&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005191053392400109415&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005211157151800103412&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005211450041480105610&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005201337434240108958&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005191254201240106694&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005210520009760109369&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005191448459080105452&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005181325461240104132&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005151206339920108810&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005131516459960108349&lcode=00&page=3&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005112023505840103658&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005121428429080105042&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005111344250120108062&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005121414579760106112&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005081746494400107759&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005061802337600103153&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005061211323520102516&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004291529352000102177&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202005041121249760107393&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004271405016960107020&lcode=00&page=4&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004281551598200102575&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003171347022040102110&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004241031049280108838&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004221739513600109219&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004231553321240107913&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004211509092160108215&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004201125361480105051&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004171555177040103458&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004171521571000103815&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004160940278960108039&lcode=00&page=5&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004171004167920106592&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004140921543720103841&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004131438380040109426&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004160821258980102989&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004141425476480104637&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004141010044400103657&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004131535327200101172&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004101806296280103990&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004131202055440104151&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004091408526360105272&lcode=00&page=6&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004081306351120103242&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004091422137520104938&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004061712462040105342&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004070952465280103062&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004021628116920101115&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202004011103520320102789&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003311147294280109019&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003271128388200108933&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003242247086240102585&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003251138470080101233&lcode=00&page=7&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003231336249520103792&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003231341219960102491&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003231017537920102464&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003181823070640102117&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003191414420240103079&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003171559289080109053&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003190552301760101433&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003171546219000108027&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003171528553520107511&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003161112543160102072&lcode=00&page=8&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003171456573040107224&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003161008350080103431&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003121843323120104425&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003131122036720105160&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003101508338720105731&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003091149248960105471&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003051835128200103457&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003051700204920102074&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003031544375960104627&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003041928400560106676&lcode=00&page=9&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003031331217840101662&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003021507214760102646&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003030940253360108036&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003030917445160104177&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003021438471200105185&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003021032481240103635&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003021401565840106077&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003021209594000103450&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202003020811013180108126&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002271451091680106475&lcode=00&page=10&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002281203060080105094&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002191938389920107911&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002241547267600106273&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002201807018200109081&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002211614278000102936&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002211358444200108912&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002201439095200108049&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002121353319400107169&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002111112283240108975&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002101400364320102177&lcode=00&page=11&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002101556092440106485&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002071450248160102150&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002061450198680107141&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002041425090200102912&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002050957532400106084&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002031011563200109367&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202002041135565840107619&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001281309159520107485&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001291432230280102055&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001291407534480108581&lcode=00&page=12&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001281005384760103117&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001281258572520108430&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001221812135280104869&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001231027087320104963&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001221757149720104257&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001231103585360109637&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001221205555440104036&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001221708174600107967&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001171321128440104265&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001161435265120103176&lcode=00&page=13&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001161318494240102174&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001151019293440107624&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001141326447240108389&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001131438274240103921&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001081355033200105071&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001070931456200106096&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001071538437520104422&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001071003174360105840&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001031806043360101075&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001061014453960108678&lcode=00&page=14&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001061737410360103832&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202001021507426880104476&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912300011579960105573&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912261345584800107233&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912201421597760105089&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912181123004560104181&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912171512306360103671&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912131121404680106081&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912100028054760108736&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912060853445820106316&lcode=00&page=15&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912081652388440106554&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912061429043760103554&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201912031501035760105613&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911290100057380003540&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911290100057710003563&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911280100055650003429&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911200100037490002319&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911200100037770002333&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911220100043680002696&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911220100043810002704&lcode=00&page=16&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911190100033560002081&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911190100034310002127&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911190100035870002219&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911180100031890001973&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911170100030290001880&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911180100032850002028&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911140100026750001657&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911140100027410001695&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911140100026710001653&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911140100025930001612&lcode=00&page=17&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911140100027160001686&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911070100012940000794&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911010100001710000112&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911010100001610000104&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201911010100002040000135&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910290100054590003391&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910310100059380003693&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910310100060780003780&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910280100050290003131&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910240100044550002773&lcode=00&page=18&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910160100027240001703&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910220100037990002368&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910210100035090002191&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910180100031850001993&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910160100027000001688&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910150100023040001433&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910110100017120001073&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910100100015050000946&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910070100010440000659&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910020100004940000311&lcode=00&page=19&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910020100004850000304&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909300100053190003308&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909240100040020002503&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201910010100001020000068&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909060100013080000819&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909030100003620000230&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909190100032670002022&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909180100029100001799&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909170100025410001565&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909170100025740001579&lcode=00&page=20&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909160100024040001483&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909110100021050001305&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909110100020710001285&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909090100014870000921&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909090100013840000861&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909020100001300000082&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908290100053350003295&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909030100003150000196&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909030100003040000186&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201909020100002870000179&lcode=00&page=21&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908270100047510002927&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908270100047070002895&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908200100034470002132&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908120100021720001352&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908090100017330001081&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908090100019240001197&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908070100012820000798&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908070100012440000777&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908050100006790000430&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908020100005800000370&lcode=00&page=22&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908010100002840000182&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908020100003830000253&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201908010100001600000098&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907290100057690003621&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907260100054910003448&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907260100053220003338&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907260100053860003377&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907180100036170002249&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907150100028580001769&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907160100029760001847&lcode=00&page=23&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907050100012570000793&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907050100012420000784&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907040100010540000667&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907040100009880000622&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907030100007770000490&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907020100004290000266&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907020100004140000257&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201906280100050890003225&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907030100007010000445&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201906280100050570003199&lcode=00&page=24&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907020100002460000152&lcode=00&page=25&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201906300100051170003240&lcode=00&page=25&svccode=00",
]

kospi_companies = yield_kospi_companies()
count_spinoffs(kospi_companies, spinoff_articles_list)
"""
