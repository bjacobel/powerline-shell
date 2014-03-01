class Color(DefaultColor):
    USERNAME_FG = 19  # dark blue
    USERNAME_BG = 240
    USERNAME_ROOT_BG = 124

    HOSTNAME_FG = 75  # light blue
    HOSTNAME_BG = 238

    REPO_CLEAN_BG = 118  # a light green color
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 208  # orange
    REPO_DIRTY_FG = 0  # black

    JOBS_FG = 39
    JOBS_BG = 238

    CMD_PASSED_BG = 236
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 161
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 22  # dark green

    VIRTUAL_ENV_BG = 35  # a mid-tone green
    VIRTUAL_ENV_FG = 00

    RUBY_VERSION_BG = 35 # same as for virtualenvs
    RUBY_VERSION_FG = 00

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 31  # blueish
    HOME_FG = 15  # white
    PATH_BG = 237  # dark grey
    PATH_FG = 250  # light grey
    CWD_FG = 254  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 124
    READONLY_FG = 254

    SSH_BG = 166 # medium orange
    SSH_FG = 254