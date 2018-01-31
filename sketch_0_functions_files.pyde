from Saver import saves
N_PHI = 30*3
N_save = N_PHI
fadeamt = .004   #min = .004

def setup():
    global saver
    saver = saves(N_PHI, N_save)

def draw():
    ### fading
    blendMode(SUBTRACT)
    noStroke()
    fill(fadeamt)
    rect(0,0,width,height)
    blendMode(BLEND)
    ### saving
    saver.save_frame()

def mouseClicked():
    saver.onClick()

#### loops h around 1
def hloop(h):
    if not(0<=h<1): return h - floor(h)
    else: return h

### custom rounding
def myround(x, base):
    return base * round(float(x)/base)

###############
# TILED NOISE #
###############

def nice(x,y):
    xp = 1.*x/wd
    yp = 1.*y/ht
    h00 = noise(x*nS,y*nS)
    h01 = noise(x*nS,(y+ht)*nS)
    h10 = noise((x+wd)*nS,y*nS)
    h11 = noise((x+wd)*nS,(y+ht)*nS)
    h = xp*yp*h00 + xp*(1-yp)*h01 + \
        (1-xp)*yp*h10 + (1-xp)*(1-yp)*h11
    return h