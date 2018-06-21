from Saver import saves
import itertools
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
    
def keyPressed():
    if key == 's': saver.onClick()

#### loops h around 1
def hloop(h):
    if not(0<=h<1): return h - floor(h)
    else: return h

### custom rounding
def myround(x, base):
    return base * round(float(x)/base)

### Use instead of nested for
for i, j in itertools.product(xrange(ni), xrange(nj)):
    pass

###############
# TILED NOISE #
###############

def n2d(x,y,W=wd,H=ht,nsx=nSx,nsy=nSy):
    xp = 1.*x/W
    yp = 1.*y/H
    h00 = noise(x*nsx,y*nsy)
    h01 = noise(x*nsx,(y+H)*nsy)
    h10 = noise((x+W)*nsx,y*nsy)
    h11 = noise((x+W)*nsx,(y+H)*nsy)
    h = xp*yp*h00 + xp*(1-yp)*h01 + \
        (1-xp)*yp*h10 + (1-xp)*(1-yp)*h11
    return constrain(map(h,.1,.8,0,1),0,1)

def n3d(x,y,t,W=wd,H=ht,TT=N_PHI,nsx=nSx,nsy=nSy,nst=nT):
    xp = 1.*x/W
    yp = 1.*y/H
    tp = 1.*t/TT
    h000 = noise(t*nst,x*nsx,y*nsy)
    h001 = noise(t*nst,x*nsx,(y+H)*nsy)
    h010 = noise(t*nst,(x+W)*nsx,y*nsy)
    h011 = noise(t*nst,(x+W)*nsx,(y+H)*nsy)
    h100 = noise((t+TT)*nst,x*nsx,y*nsy)
    h101 = noise((t+TT)*nst,x*nsx,(y+H)*nsy)
    h110 = noise((t+TT)*nst,(x+W)*nsx,y*nsy)
    h111 = noise((t+TT)*nst,(x+W)*nsx,(y+H)*nsy)
    h = tp*xp*yp*h000 + tp*xp*(1-yp)*h001 + \
        tp*(1-xp)*yp*h010 + tp*(1-xp)*(1-yp)*h011 + \
        (1-tp)*xp*yp*h100 + (1-tp)*xp*(1-yp)*h101 + \
        (1-tp)*(1-xp)*yp*h110 + (1-tp)*(1-xp)*(1-yp)*h111
    return constrain(map(h,.1,.8,0,1),0,1)

### signum function

def sign(s):
    if s >= 0: return 1
    else: return -1