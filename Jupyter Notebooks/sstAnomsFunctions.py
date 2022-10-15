def North_Atlantic():
    regionName = 'North Atlantic'
    savePathAnoms = 'NorthAtlantic/'
    fileNameAnoms = 'natl_sstAnoms_'
    north = 63
    south = 0
    east = 360
    west = 250
    extent = [-110,0,0,63]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent

def Gulf_of_Mexico():
    regionName = 'Gulf of Mexico'
    savePathAnoms = 'GulfofMexico/'
    fileNameAnoms = 'GOM_sstAnoms_'
    north = 31
    south = 15
    east = 285
    west = 260
    extent = [-100,-75,15,31]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent

def World():
    regionName = 'World'
    savePathAnoms = 'World/'
    fileNameAnoms = 'world_sstAnoms_'
    north = 90
    south = -90
    east = 360
    west = 0
    extent = [-180,180,-90,90]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent

def Arctic():
    regionName = 'Arctic'
    savePathAnoms = 'Arctic/'
    fileNameAnoms = 'arctic_sstAnoms_'
    north = 90
    south = 50
    east = 360
    west = 0
    extent = [-180,180,60,90]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent

def Antarctic():
    regionName = 'Antarctic'
    savePathAnoms = 'Antarctic/'
    fileNameAnoms = 'antarctic_sstAnoms_'
    north = -50
    south = -90
    east = 360
    west = 0
    extent = [-180,180,-90,-60]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent

def Equatorial_Pacific():
    regionName = 'Equatorial Pacific'
    savePathAnoms = 'EquatorialPacific/'
    fileNameAnoms = 'epac_sstAnoms_'
    north = 25
    south = -25
    east = -78
    west = -267
    extent = [-15,102,-25,25]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent

def Tropical_Atlantic():
    regionName = 'Tropical Atlantic'
    savePathAnoms = 'TropicalAtlantic/'
    fileNameAnoms = 'tropAtl_sstAnoms_'
    north = 38
    south = 0
    east = 345
    west = 285
    extent = [-75,-15,0,38]
    
    return regionName, savePathAnoms, fileNameAnoms, north, south, east, west, extent