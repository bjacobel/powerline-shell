import subprocess


def add_ruby_version_segment():
    try:
        if os.environ.has_key("GEM_HOME"):
            gem = os.environ["GEM_HOME"].split("@")

            # Only display info if a non-default gemset is present
            if len(gem) > 1:
                p1 = subprocess.Popen(["ruby", "-v"], stdout=subprocess.PIPE)
                p2 = subprocess.Popen(["sed", "s/ (.*//"], stdin=p1.stdout, stdout=subprocess.PIPE)
                version = " {} {} ".format(p2.communicate()[0].rstrip(), gem[1])

                bg = Color.RUBY_VERSION_BG
                fg = Color.RUBY_VERSION_FG
                
                powerline.append(version, fg, bg)
    except OSError:
        return

add_ruby_version_segment()
