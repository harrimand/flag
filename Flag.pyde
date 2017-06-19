#Darrell Harriman  harrimand@gmail.com  06/18/2017
#Processing IDE in Python Mode
#Draw US Flag based on dimensions at www.usflag.org/flagspecs.html
#Flag is scaled according to flagHeight
#border will size the window so there is a border on the sides, top and bottom of flag.

flagHeight = 800
border = 20

def settings():
    sizeW = (int)(flagHeight * 1.9 + 2 * border)
    size(sizeW, flagHeight + 2 * border, P2D)

def setup():
    global star
    r = .0313 * flagHeight 
    background(224, 224, 255)
    star = makeStar(r)

def draw():
    F = .054 * flagHeight    # Star Vertical Row Spacing
    H = .063 * flagHeight    # Star Horizontal Spacing
    C = .5385 * flagHeight   # Union Height
    D = .76 * flagHeight     # Union Width
    L = .0769 * flagHeight   # Stripe Width
    B = 1.9 * flagHeight     # Flag Width

# White Flag Background
    noStroke()
    fill(255, 255, 255)
    rect(border, border, B, flagHeight)    #Flag White Background

# Union Background
    fill(0, 33, 71)
    rect(border, border, D, C)    #Union Background

# Union Stars on Odd rows
    for r6 in range(1, 11, 2):
        for s in range(1, 13, 2):
            shape(star, s * H + border, r6 * F + border)

# Union Stars on Even rows
    for r4 in range(2, 10, 2):
        for s in range(2, 12, 2):
            shape(star, s * H + border, r4 * F + border)

# Red Stripes
    fill(187, 19, 62)
    for stpos in range(0, 14, 2):
        stLeft = D + border if stpos < 8 else border
        stWidth = B - D if stpos < 8 else B
        rect(stLeft, stpos * L + border, stWidth, L)

    noLoop()

def makeStar(r):
    """  Vertex scalers are calculated for a 5 point star using points at radius r 
    evenly distributed in 72 degree increments.  Inner points are 36 degrees from 
    outer points.  x scalers (h1 - h5) and y scalers (v1 - v5) were pre-calculated 
    using the cos(), sin() functions and intersect points for lines connecting 
    outer points. 
    """
    h1 = 0
    h2 = .224514
    h3 = .363271
    h4 = .587785
    h5 = .951057
    v1 = -1
    v2 = -.309017
    v3 = .118034
    v4 = .381966
    v5 = .809017
    st = createShape()
    st.beginShape()
    st.fill(255,255,255)
    st.noStroke()
    st.vertex(h1*r, v1*r)
    st.vertex(h2*r, v2*r)
    st.vertex(h5*r, v2*r)
    st.vertex(h3*r, v3*r)
    st.vertex(h4*r, v5*r)
    st.vertex(h1*r, v4*r)
    st.vertex(-h4*r, v5*r)
    st.vertex(-h3*r, v3*r)
    st.vertex(-h5*r, v2*r)
    st.vertex(-h2*r, v2*r)
    st.endShape(CLOSE)
    return st