"""BIP39 mnemonic generation (real functionality)"""
import os, hashlib

WORDS = """abandon ability able about above absent absorb abstract absurd abuse
access accident account accuse achieve acid acoustic acquire across act action
actor actress actual adapt add addict address adjust admit adult advance advice
aerobic affair afford afraid again age agent agree ahead aim air airport aisle
alarm album alcohol alien all alley allow almost alone alpha already also alter
always amazing among amount amused analyst anchor ancient anger angle angry
animal announce annual another answer antenna antique anxiety any apart apology
appear apple approve april arch arctic area arena argue arm armor army around
arrange arrest arrive arrow art artifact artist ask aspect assault asset assist
assume asthma athlete atom attack attend attitude attract auction audit august
aunt author auto autumn average avocado avoid awake aware awesome awful awkward
axis baby bachelor badge bag balance balcony ball bamboo banana banner bar barely
bargain barrel base basic basket battle beach bean beauty because become beef
before begin behave behind believe below belt bench benefit best betray better
between beyond bicycle bid bike bind biology bird birth bitter black blade blame
blanket blast bleak bless blind blood blossom blouse blue blur blush board boat
body boil bomb bone bonus book boost border boring borrow boss bottom bounce box
boy bracket brain brand brass brave bread breeze brick bridge brief bright bring
brisk broccoli broken bronze broom brother brown brush bubble buddy budget buffalo
build bulb bulk bullet bundle bunker burden burger burst bus business busy butter
buyer buzz cabbage cabin cable cactus cage cake call calm camera camp can canal
cancel candy cannon canoe canvas canyon capable capacity capital captain capture
carbon cardinal care career careful carpet carry case cash casino castle casual
catch category cattle caught cause ceiling celery cement census century ceramic
ceremony certain chair chalk champion change chaos chapter charge chase chat cheap
check cheese chef cherry chest chicken chief child chimney choice choose chronic
chuckle chunk churn cigar cinnamon circle citizen civil claim clap clarify claw
clay clean clerk clever click client cliff climb clinic clip clock clogs close
cloth cloud clown club clump cluster clutch coach coast coconut code coffee coil
coin collect color column combine come comfort comic common company concert conduct
confirm congress connect consider control convince cook cool copper copy coral core
corn correct cost cotton couch country couple course cousin cover coyote crack
cradle craft crane crash crater crawl crazy cream credit creek crew cricket crime
crisp critic crop cross crouch crowd crucial cruel cruise crumble crunch crush cry
crystal cube culture cup cupboard curious current curtain curve cushion custom cute
cycle dad damage damp dance danger daring dark dash date daughter dawn day deal
debate debris decade december decide decline decorate decrease deer defense define
defy degree delay deliver demand demise denial dentist deny depart depend deposit
depth deputy derive describe desert design desk despair destroy detail detect
develop device devote diagram dial diamond diary dice diesel diet differ digital
dignity dilemma dinner dinosaur direct dirt disagree discover disease dish dismiss
display distance distinct divorce dizzy doctor document dog doll dolphin domain
donate donkey donor dose double dove dragon drama drastic draw dream dress drift
drill drink drip drive drop drum dry duck dumb dune during dust dutch duty dwarf
dynamic eager eagle early earn earth easily east easy echo ecology economy edge
edit educate effort egg eight either elbow elder electric elegant element elephant
elevator elite else embark embody embrace emerge emotion employ empower empty enable
enact end endless endorse enemy energy enforce engage engine enhance enjoy enlist
enormous enough enrich enroll ensure enter entire entry envelope episode equal equip
erase erect erosion error erupt escape essay essence estate eternal ethics evidence
evil evoke evolve exact example excess exchange excite exclude excuse execute
exercise exhaust exhibit exile exist exit exotic expand expect expire explain expose
express extend extra eye eyebrow fabric face faculty fade faint faith fall false
fame family famous fan fancy fantasy farm fashion fat fatal father fatigue fault
feature february federal fee feed feel female fence festival fetch fever few fiber
fiction field figure file film filter final find fine finger finish fire firm first
fiscal fish fit fitness fix flag flame flash flat flavor flee flight flip float
flock floor flower fluid flush fly foam focus fog foil fold follow food foot force
foreign forest forget fork fortune forum forward fossil foster found fox fragile
frame frequent fresh friend fringe frog front frozen frugal fruit frustrate fuel
fun funny furnace fury future gadget gain galaxy gallery game gap garage garbage
garden garlic garment gas gasp gate gather gauge gaze general genius genre gentle
genuine gesture ghost giant gift giggle ginger giraffe girl give glad glance glare
glass glide glimpse globe gloom glory glove glow glue goat goddess gold good goose
gorilla gospel gossip govern gown grab grace grain grant grape grass gravity great
green grid grief grit grocery group grow grunt guard guess guide guilt guitar gun""".split()

def generate(strength=128):
    """Generate a random BIP39 mnemonic phrase (12 or 24 words)"""
    entropy = os.urandom(strength // 8)
    h = hashlib.sha256(entropy).digest()
    bits = bin(int.from_bytes(entropy, 'big'))[2:].zfill(len(entropy)*8) + bin(h[0])[2:].zfill(8)
    idx = [int(bits[i:i+11], 2) for i in range(0, len(bits), 11)]
    return " ".join(WORDS[i] for i in idx[:len(idx)-1])

def validate(phrase):
    """Validate a BIP39 mnemonic phrase (checks wordlist membership)"""
    words = phrase.lower().split()
    if len(words) not in (12, 15, 18, 21, 24):
        return False
    return all(w in WORDS for w in words)
