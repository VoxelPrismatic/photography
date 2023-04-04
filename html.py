folder = input("Folder: ")
patreon = input("Patreon post link: ")
main = input("Title image: ")
desc = input("Description: ")

st = f"""




<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta charset="utf-8" />

        <!-- PRELOAD -->
        <link rel="preload" src="/prizm.dev/assets/script/min.js" type="text/javascript" as="script"/>
        <link rel="preload" src="/prizm.dev/assets/css/priz-pink.css" type="text/css" as="stylesheet"/>
        <link rel="preload" src="/prizm.dev/assets/css/fonts.css" type="text/css" as="stylesheet"/>
        <link rel="preload" src="/prizm.dev/assets/css/ubuntu/Ubuntu-BI.ttf" type="font/sfnt" as="font"/>
        <link rel="preload" src="/prizm.dev/assets/css/ubuntu/Ubuntu-RI.ttf" type="font/sfnt" as="font"/>
        <link rel="preload" src="/prizm.dev/assets/css/ubuntu/Ubuntu-B.ttf" type="font/sfnt" as="font"/>
        <link rel="preload" src="/prizm.dev/assets/css/ubuntu/Ubuntu-R.ttf" type="font/sfnt" as="font"/>
        <link rel="preload" src="/prizm.dev/assets/image/webp/priz_pink.webp" type="image/webp" as="image"/>

        <!-- STATIC BETWEEN PAGES -->
        <meta name="theme-color" content="#FF0088">
        <meta name="author" content="PRIZ ;]" />

        <meta name="twitter:site" content="@VoxelPrismatic">
        <meta name="twitter:creator" content="@VoxelPrismatic">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:image" content="https://voxelprismatic.github.io/prizm.dev/assets/image/photography/laguna/{main}.webp-med.webp" />

        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://voxelprismatic.github.io/prizm.dev/photos/{folder}" />
        <meta property="og:site_name" content="PRIZ ;]">

        <meta property="og:image" content="https://voxelprismatic.github.io/prizm.dev/assets/image/webp/favi/priz_pink.webp" />
        <meta property="og:image:type" content="image/webp" />
        <meta property="og:image:width" content="256" />
        <meta property="og:image:height" content="256" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <link rel="icon" type="image/png" href="/prizm.dev/assets/image/favicon.png" />
        <link rel="stylesheet" type="text/css" id="priz_neon_css" href="/prizm.dev/assets/css/priz-pink.css" />

        <!-- DYNAMIC BETWEEN PAGES -->
        <meta property="og:title" content="{folder.upper()} ;]" id="title" />
        <title>{folder.upper()} ;]</title>
        <meta property="og:description" content="{desc}" />
        <meta name="description" content="{desc}" />
""" + """
        <style type="text/css">
            #head {
                top: -100px !important;
            } img {
                max-width: 100%;
            } #logo > img:hover {
                cursor: pointer;
            }
        </style>
""" + f"""
    </head>
    <body class="bgcolor" style="background-color: #221115;">
        <div id="logo">
            <img src="/prizm.dev/assets/image/webp/priz_pink.webp" alt="[prizm logo]" id="truelogo" tabindex="-1" height="156px" onclick="location='/prizm.dev/photos'"/>
        </div>
        <h1 id="head" tabindex="-1">{folder.upper()} ;]</h1>
        <div id="content">
            <div class="sect" style="transition: none 0s ease 0s;">
                <h1 onclick="linkMe(this);" id="{folder.upper()}">#] {folder.upper()}</h1><br>
                This is an album filled with backdrops. All of these were taken with the small
                Galaxy S8 [SM-G950U] and watermarked for display. If you would like to receive a
                copy without the watermark and with the metadata [except for location], please
                support me on <a href="https://www.patreon.com/posts/pics-laguna-59349832" target="_blank">Patreon</a>.
                Maybe a few too many birbs. Fun fact: only a few images were taken in Laguna Beach lol<br><br>
\x1b[1;5;7;91m                ^^CHANGE THIS DESCRIPTION^^                          .\x1b[0m

                <line></line><br>
"""

a, b = ".", "."
while a and b:
    a = input("Pic name: ")
    if not a:
        break
    c = a
    for x in "[]#:.?&":
        c = c.replace(x, "")
    c = c.replace(" ", "-")
    b = input("Pic file: ")
    st += f"""
                <h2 onclick="linkMe(this);" id="{c}">#] {a}</h2><br>
                <img controls="true" alt="{b}.webp" title="birb1.webp" data-src="/prizm.dev/assets/image/photography/{folder}/{b}.webp"><br><br>
"""

st += f"""

                <div style="text-align: center;">
                    <div style="height: 0px; transition: none 0s ease 0s;" id="spacer"></div>
                    <sub id="footer">
                        <br />
                        <br />
                        <b style="font-size: larger;">BY PRIZ WITH WINKY BRACKET FACE ;]</b><br />
                        <span id="links_and_sources" tabindex="-1">
                            <a href="/prizm.dev" target="" tabindex="0">Home page</a> //
                            <a id="page_source_about" target="_blank" rel="noreferrer" href="https://github.com/VoxelPrismatic/prizm.dev/blob/master/photos/{folder}.html" tabindex="0">View source</a>
                        <br />
                        <span id="copyright">© PRIZ ;], 2021</span>
                        <br>
                        <span id="funnytextthing" tabindex="-1">*loading funny text thing</span><br />
                        <br />
                    </sub>
                </div>
            </div>
        </div>

        <div style="display: none;" id="scripts">
            <script type="text/javascript">
                var theme = "pink";
                var loader = "main";
            </script>
            <a id="hiddenlink" tabindex="0"></a>
            <script type="text/javascript" src="/prizm.dev/assets/script/min.js" id="min.js"></script>
            <script type="text/javascript" src="/prizm.dev/assets/script/photos.js" id="photos.js"></script>
            <script type="text/javascript" defer>
                loadNow();
            </script>
            <link rel="stylesheet" type="text/css" href="/prizm.dev/assets/css/fonts.css">
        </div>
        <div id="jumper" onclick="jumpToEdge()">[V]</div>
    </body>
</html>
\x1b[1;5;7;91mCHANGE THE DESCRIPTION\x1b[0m
"""

print(st)
