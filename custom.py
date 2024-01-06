CCFLAGS = ['-Ilua/src', '-Isrc/lib', '-O2', '-ansi']
LIBPATH = ['lua/src']
LIBS = ['lua', 'dl', 'm']
prefix = '/mingw'
#build_dev=1
tolua_bin = 'tolua++'
tolua_lib = 'tolua++'
TOLUAPP = 'tolua++'