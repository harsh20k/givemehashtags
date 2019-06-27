from flask  import Flask
from collections import Counter

app = Flask(__name__)
@app.route('/')
def index():


    contents = """#serverlife #serverproblems #serverprobs #servers #servermemes #webcomicseries #stickfigure #dontreadmytags #webcomics #doodlesketch #comicstyle #quickdoodle #quicksketches #comicartwork #comicpanel #comicpanels #comicstrip #comicstrips #funnycomics #funnycomic #comic #stickman #waiter #dailycomic #dailycomics #igcomic #igcomics #webtoon #cartoonistsofinstagram #cartoony

    #relatables #relatablememe #relatablepost #relatablecomics #comicstrip #comicstrips #stickfigures #relatablememes❌ #funnyart #funnycomicstrips #funnycomic #funnycomics #comicseries #dailycomics #dailycomic #doodlesketch #comicgram #comicpage #igcomics #igcomicfamily #makingcomics #comicstyle #cartoonist #comic #cartoonistsofinstagram #cartoonists #cartoonistsoninstagram #annoyingpeople #sadmeme #counterintuitive

    #stickfigures #comicpage #lovecomics #sliceoflife #comicgram #minimalisme #instacomics #webcomic #webcomics #dailycomic #artmeme #webtoon #webtoons #makingcomics #comicdrawing #comicartist #fumetti #seemedoodle #doodlesketch #sketchdoodle #originalcomic #indiecomics #independentcomics #indiecomic #independentcomic #relatablecomics #funnycomic #funnycomics #webcomicseries #artoftheday🎨

    #webcomix #makecomics #webcomic #comicstyle #igcomicfam #igcomic #igcomics #comicpanels #comicpanel #comicpage #comicgram #doodles #doodlesketch #dailycomic #dailycomics #funnycomics #funnycomic #funnycomicstrips #funnyart #comicstrips #relatablecomics #relationshipposts #relationshipmemes #relatablememe #stickfigure #dontreadmytags #webcomicseries #commitmentissues #breakups #breakupssuck

    #pencilonly #pencilonpaper #relatablecomics #comicstrip #stickfigures #relatablememe #relatablememes❌ #funnyart #funnycomicstrips #funnycomic #funnycomics #comicseries #dailycomics #dailycomic #doodlesketch #comicgram #comicpage #igcomics #igcomicfamily #makingcomics #occomic #comicstyle #webcomicseries #webcomic #cartoonist #comic #comics #doodlez #cartoonistsofinstagram #cartoonists

    #relatablepost #relatables #relatableaf #relatabletumblr #rudepeople #relatablecomics #comicstrip #stickfigure #relatablememes #comicstrips #funnyart #comicdrawing #dailycomics #instacomic #webcomicseries #doodleoftheday #funnycomic #funnycomics #sketchingdaily #quicksketches #quickart #comicstyle #comicpanel #igcomics #igcomic #igcomicfam #tumblrmemes #comical #comicartist #comicpage

    #makecomics #webcomics #webcomicseries #comicstyle #igcomicfam #igcomic #igcomics #comicpanels #comicpanel #comicpage #comicgram #doodles #doodlesketch #dailycomic #dailycomics #funnycomics #funnycomic #funnycomicstrips #funnyart #comicstrips #relatablecomics #relatablememe #introversion #introvert #introverts #introversion #introvertmemes #introvertproblems #webcomix #introverted

    #webcomicseries #dailycomics #boyfriendmemes #girlfriendmemes #relationshipmemes #relationshipposts #tagyourbestie #tagbae #cutecomics #lovecomics #ambiguous #stickman #comicstrip #comicstrips #originalcomic #comicsart #indiecomic #independentcomics #webcomics #comicstagram #comiclife #sketchpad #comicpanel #comicpanels #igcomic #igcomics #instacomics #instacomic #lovecomic

    #stickfigure #pridefest #comicpage #comic #doodle #doodles #doodlesketch #instacomic #instagay #instagays #webcomicseries #dontreadmytags #comicgram #comicstrip #comicstrips #comicpanel #comicpanels #makecomics #dailycomics #webtoon #cartoonists #cartoonistsofinstagram

    #videogamemusic #webcomicseries #doodlesunited #comicgram #cartoonist #cartoonists #cartoonistsofinstagram #blackandwhite #stickman #stickfigure #sketchings #webtoon #digitalcomic #digitalcomics #dailycomics #dailydrawings #stickperson #sketchpad #comicstyle #comicstrips #comicstrip #comicpanel #comicpanels #igcomics #igcomic #igcomicfamily #igcomicfamily #doodlesofinsta #funnycomic #funnycomics

    #webcomix #webcomicseries #dontreadmytags #stickfigure #introvert #introvertproblems #introvertmemes #introverts #introversion #relatablememe #relatablecomics #comicstrips #funnyart #funnycomicstrips #funnycomic #funnycomics #dailycomics #dailycomic #doodlesketch #doodles #comicgram #comicpage #comicpanel #comicpanels #igcomics #igcomic #igcomicfam #comicstyle #webcomic #makecomics

    #dailycomics #mindblown #makingcomics #comicsofinstagram #digitalcomics #digitalcomic #comicstyle #comicdrawing #instacomic #igcomics #comics #stickfigure #dailydoodles #art_minimal #sketchesofinstagram #doodle #artmeme #pencilsketches #quickart #comicsketch #doodleoftheday #funnycomics #funnycomic #pencilonly #blankface #webcomicseries #igcomicfam #igcomicfamily #relatablecomics #originalcomic

    #relatablecomics #comicstrip #stickfigure #relatablememes #comicstrips #funnyart #funnycomicstrips #funnycomics #funnycomic #dontreadmytags #dailycomics #dailycomic #dailycomicstrip #comicsdaily #doodlesketch #doodles #relatablecomic #comicgram #comicpage #comicpanel #comicpanels #igcomics #igcomicfam #igcomicfamily #makingcomics #occomic #comicstyle

    #boyfriendmemes #girlfriendmemes #relationshipmemes #tagbae #tagsomeone #tagyourbae #cutecomic #lovecomics #ambiguous #blankface #stickman #comics #comic #comicstrip #comicstrips #originalcomic #relatablememes #comicsart #indiecomics #independentcomics #webcomic #webcomics #comicstagram #comiclife #pencil_sketch #pencildrawings #comicsofinstagram #comicpanel #igcomics #instacomics

    #comicstrips #sketchpad #comicartwork #comicbooknerd #webcomics #comicnerd #doodlebug #webtoon #bfcomicsspotlight #digitalcomics #blankface #digitalillustration #makecomics #comicartist #doodlez #darkcomedy #darkhumormemes #cartoonillustration #comichumor #comiccollector #fastsketch #sketchings #dailydrawings #stickperson #stickman #officememes #officeparty #comics #doodlesunited

    #stickfigure #stickfigures #blankface #funny #comicpage #ambiguous #palindrome #palindromes #grammarhumor #grammar #grammarpolice #englishgrammar #comicgram #comicstagram #comicsketch #comicpanel #dailycomic #drawingcomics #dailycomics #comicoftheday #digitalcomics #blackandwhite #pencilonly #instacomics #comicstrip #comicsofinstagram #comicartwork

    #facereveal #facerevealed #doodlesunited #cartoonhumor #1000followers #1000 #vibes #simplecomic #blankface #lol #fun #lifeisamazing #artistsoninstagram #artistsoninsta #artistsonig #webcomicseries #stickfigureart #webcomix #comic #comics #comicdrawings #comicpanel #comicpanels

    #comicsofinstagram #relatableart #relatablememe #relatablememes #relatablememes❌ #relatablecomic #relatablecomics #art #comic #comics #stickfigures #stickfigure #stickfigureart #instadoodles #cartoonistsofinstagram #dontreadmytags #ocdoodle #drawthisinyourstyle #drawthisinyourstylechallenge #drawthis #relatable #cutecomic #artmeme #artmemes #webtoon #funnyart #doodleoftheday #sketchingdaily #dailycomics

    #indianmemes #bobsandvagene #indianpeople #indianpeoplefacebook #pewdiepie #pewdiepiememes #pewdipie #subscribetopewdiepie #subtopewdiepie #dailycomics #dailycomic #comics #comic #doodle #doodles #doodle_art #art #stickfigures #stickfigure #webcomicseries #dontreadmytags #mydoodles #doodleaday #doodlesketch #doodle_art #igcomics #igcomicfam #doodlegram #comicpanel #comicstrips

    #jesusmemes #christianmemes #christianmeme #comics #dontreadmytags #webcomicseries #webcomic #webcomics #webcomicartist #quickdoodle #drawingsofinstagram #drawingstuff #drawig #draws #doodle #doodleart #doodles #doodlesketch #doodlesunited #drawthisinyourstyle #drawinyourstyle #drawing✏ #draw🎨 #webcomix #comix #comicstyle #stickfigures #stickfigure #stickfigureart

    #relatablecomics #comicstrip #stickfigure #relatablememes #comicstrips #funnyart #funnycomicstrips #funnycomics #funnycomic #funnyaf #dontreadmytags #memestagram #dailycomics #comicsdaily #doodle #doodles #relatable #relatablecomic #comicgram #comicpage #igcomics #igcomicfam #igcomicfamily #makingcomics #occomic #comicstyle #webcomicseries

    #veganmemes #vegans #veganaf #stickfigure #stickfigures #comicgram #relatablecomics #relatablecomic #relatablememe #relatablememes #webtoon #webcomic #webcomics #cartoonistsofinstagram #cartoonist #cartoony #cartoonists #dailycomic #dailycomics #doodle #doodles #funnycomic #funnycomics #comic #comics #drawdrawdraw #igcomics #humor #funnymeme

    #comic #comics #doodle #doodles #stickfigure #stickfigures #comicpage #relatable #relatablememes #dailycomics #quickart #doodleaday #comix #comicpage #doodlegram #newcomic #sketches #doodlesketch #pencil_art #pencildraw #artmeme #drawingstuff #drawingsofinstagram #funnycomics #funnycomic #doodle_art #doodleart #doodleartist #artaccount

    #stickfigure #stickfigures #funny #comicpage #lgbtmemes #lgbtqmemes #lgbtmeme #lgbtqmeme #makingcomics #comicdrawing #art #doodle #doodles #oroginalcomics #cartoonistsofinstagram #twistending #ambiguous #comicgram #instacomic #webcomic #webcomics #dailycomic #artmeme #webtoon #relatablecomics #relatablecomic #relatablememes #relatable #relatablememe

    #funnyart #humor #pencildraw #drawing #doodlegram #pencil_art #art #pencilart #webtoon #relatablecomics #instadoodles #newcomic #digitaldoodles #relatable #comicstrips #stickfigure #originalcomic #drawingsketch #doodles #relatablememes #perspective #pencildrawings #drawingsofinstagram #comicpanel #draw #pencildrawing #cartoonistsofinstagram #dontreadmytags #ocsketch

    #funny #mydoodle #comic #minimalisme #webcomic #sketch #dailycomic #myartstyle #comix #comicdrawing #sketchings #comicstrips #webcomics #pencilonly #drawdrawdraw #funnycomic #comicgram #minimaldrawing #digitalcomic #draws #igcomics #quickdoodles #digitaldoodle #webcomicseries #comicpage #tallproblems #tallgirlproblems #tallpeopleproblems #tallgirlprobs #tallguyproblems

    #dailycomics #makingcomics #comicsofinstagram #digitalcomics #comicstyle #comicdrawings #instacomic #dailydoodles #art_minimal #sketchesofinstagram #minimalinsta #doodle #stickfigures #artmeme #pencilsketches #quickart #minimal_mood #comicsketch #sketchingdaily #quickdoodle #funnycomics #doodleoftheday #pencilonly #doodleaday #sharktank #sharktankabc #sharktanknation #entrepreneurn #entreprenuer

    #illustration #digitaldoodle #draw #drawing #sketch #comix #instadoodles #doodlegram #comic #comics #stickfigure #funnycomic #funnycomics #comicstrip #newcomic #dailycomic #webtoon #jobinterview #jobseeker #recruiterlife #relatablecomic #relatablecomics #newcomics #funny #comicstrip #comicstrips #originalcomic #instacomic #comicsofinstagram #webcomicartist

    #stickfigure #stickfigures #funny #comicpage #boyfriend #boyfriendmemes #lovecomics #twistending #ambiguous #comicgram #instacomic #webcomic #webcomics #dailycomic #artmeme #webtoon #makingcomics #comicdrawing #art #doodle #doodles #originalcomic #originalcomics #cartoonistsofinstagram #funnycomic #relatable #relatablememe #relatablememes #relatablecomic #relatablecomics

    #dailycomic #artmeme #uber #ubereats #makingcomics #cartoonistsofinstagram #comicstyle #digitalcomic #digitalcomics #funnycomic #cartooning #newcomic #instacomic #webtoon #comicstrips #webcomic #webcomics #dontreadmytags #foodie #uberdriver #ubermemes #ubermeme

    #comic #comics #doodle #doodles #stickfigure #stickfigures #comicpage #basketball #basketballtime #basketballgames #basketballmemes #sports #relatable #relatablememes #relatablecomics #funny #art #comicstrips #comicstrip #athletics #games #fail #fails #meme #memes #funnymemes

    #relatablecomics #comicstrip #stickfigure #relatablememes #comicstrips #comic #comics #funny #relatable #art #melee #fgc #sports #competition #gaming #gamingmemes #doodle #doodles #funnymemes #memes #memesdaily #memestagram #funnyaf #relatablememes #funnycomic #funnycomics #funnycomicstrips #funnyart

    #comic #comics #doodle #doodles #stickfigure #stickfigures #comicpage #coke #soda #relatable #relatablememes #relatablecomics #relatablecomic #funny #art #comicstrips #comicstrip #diet #dietsoda #dietcoke

    #comicstagram #comicbites #fundrawing #originalcomic #drawoftheday #comical #comiclover #comix #comiconindia #comicstyle #artsandcrafts #art #papabear #digitalcomics #comicpanel #tnycartoons #senddoods #funnycomic #dailycomics #comicsofinstagram #comicoftheday #igcomics #webcomicseries #webcomicartist #cartoonistsofinstagram #cartooning #lovecartoons #cartoonists

    #bighugscafe #instacomic #comicillustration #webcomics #comicsofinstagram #cartoonstrip #jokesonyou #comicstrip #dailycomics #dailycomic #cutememes #wholesomemes #cartoony #dailyjokes #laughalittle #cutecomic #comicbites #webcomicstrip #webcomicz #cartoonanimals #funnycomic #funnycomics #mylifemyrules #mylifeisgood #mylifeisablessing

    #bighugscafe #instacomic #comicillustration #webcomics #comicsofinstagram #cartoonstrip #jokesonyou #comicstrips #dailycomics #dailycomic #cutememes #wholesomemes #cartoony #dailyjokes #laughalittle #cutecomic #comicbites #webcomicstrip #webcomicz #cartoonanimals #funnycomic #funnycomics #birdsofindia #funnyanimal #funnyanimalmemes #hippopotamus #businessmen #moneyproblems

    #bighugscafe #digitalcomics #comicpanel #funnycomic #dailycomics #comics #comicsofinstagram #comicoftheday #igcomics #webcomicseries #webcomicartist #cartoonistsofinstagram #cartooning #cartoonists #tnycartoons #lovecartoons #fridaycartoons #senddoods #comicstagram #comicbites #fundrawing #originalcomic #drawoftheday #comical #comiclover #comix #comicon #comicstyle

    #bighugscafe #comicstrip #comics #cartoonz #comicstrips #funnycartoons #weird #instacomics #instacomic #comic #webtoon #dailycomics #webcomic #illustration #funnyanimals #stupidfish #forgetful #forgetfulness"""

    list_contents=contents.split()
    counts = Counter(list_contents)

    ignore = ['#stickfigure', '#stickfigures', '#dontreadmytags', '#stickman', '#pencilonly', '#ambiguous', '#blankface', '#relationshipmemes', '#sketchingdaily', '#boyfriendmemes', '#sketchpad', '#sketchings', '#stickfigureart', '#quicksketches', '#minimalisme', '#relationshipposts', '#introvert', '#introverts', '#introvertmemes', '#introvertproblems', '#girlfriendmemes', '#tagbae', '#???\u200d??', '#blackandwhite', '#stickperson', '#pencilsketches', '#pencildrawings', '#drawthisinyourstyle', '#draws', '#pencil_art', '#pencildraw', '#twistending', '#sports', '#serverlife', '#serverproblems', '#serverprobs', '#servers', '#servermemes', '#waiter', '#sadmeme', '#sliceoflife', '#fumetti', '#seemedoodle', '#sketchdoodle', '#artoftheday??', '#commitmentissues', '#breakups', '#breakupssuck', '#pencilonpaper', '#rudepeople', '#introverted', '#???\u200d??pride', '#pride', '#pridemonth', '#prideparade', '#pridemonth2019', '#pride2019', '#pride??', '#pridefest', '#instagay', '#instagays', '#videogamemusic', '#pencil_sketch', '#bfcomicsspotlight', '#darkcomedy', '#darkhumormemes', '#officememes', '#officeparty', '#palindrome', '#palindromes', '#grammarhumor', '#grammar', '#grammarpolice', '#englishgrammar', '#facereveal', '#facerevealed', '#1000followers', '#1000', '#vibes', '#lol', '#fun', '#lifeisamazing', '#drawthisinyourstylechallenge', '#drawthis', '#indianmemes', '#bobsandvagene', '#indianpeople', '#indianpeoplefacebook', '#pewdiepie', '#pewdiepiememes', '#pewdipie', '#subscribetopewdiepie', '#subtopewdiepie', '#jesusmemes', '#christianmemes', '#christianmeme', '#drawinyourstyle', '#drawing?', '#draw??', '#veganmemes', '#vegans', '#veganaf', '#sketches', '#lgbtmemes', '#lgbtqmemes', '#lgbtmeme', '#lgbtqmeme', '#pencilart', '#drawingsketch', '#perspective', '#pencildrawing', '#myartstyle', '#quickdoodles', '#tallproblems', '#tallgirlproblems', '#tallpeopleproblems', '#tallgirlprobs', '#tallguyproblems', '#minimal_mood', '#sharktank', '#sharktankabc', '#sharktanknation', '#entrepreneurn', '#entreprenuer', '#jobinterview', '#jobseeker', '#recruiterlife', '#boyfriend', '#uber', '#ubereats', '#foodie', '#uberdriver', '#ubermemes', '#ubermeme', '#basketball', '#basketballtime', '#basketballgames', '#basketballmemes', '#athletics', '#games', '#fail', '#fails', '#melee', '#fgc', '#competition', '#gaming', '#gamingmemes', '#coke', '#soda', '#diet', '#dietsoda', '#dietcoke', '#papabear', '#mylifemyrules', '#mylifeisgood', '#mylifeisablessing', '#birdsofindia', '#hippopotamus', '#businessmen', '#moneyproblems', '#stupidfish', '#forgetful', '#forgetfulness']

    for word in list(counts):
        if word in ignore:
            del counts[word]

    for i in counts:
        print( "% s : % s" % (i, counts[i]), end ="\n")


    return "cccounts"

if __name__ == "__main__":
    app.run(debug=False)
