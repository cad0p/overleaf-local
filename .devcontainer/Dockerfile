# # Server Pro users:
# image: quay.io/sharelatex/sharelatex-pro

# Free version users:
FROM sharelatex/sharelatex

# # do this if the version of TexLive is not the same as sharelatex/sharelatex-base's one
# # fix TexLive version to sharelatex/sharelatex-base 's one
# # https://tex.stackexchange.com/a/429718/189950
# RUN tlmgr option repository ftp://ftp.tu-chemnitz.de/pub/tug/historic/systems/texlive/2022/tlnet-final

# # install TexLive packages
# RUN tlmgr install caption xkeyval parskip etoolbox setspace emptypage \
#   titlesec moresize transparent eso-pic subfig pgf thmtools float \
#   mathtools algorithms cleveref pdfpages lipsum pdflscape soul \
#   wrapfig eso-pic subfig booktabs svg koma-script trimspaces catchfile \
#   nth enumitem minted pygmentize

# # To convert eps to pdf (only needed if you didn't install the full version of TexLive)
# # https://tex.stackexchange.com/a/231225/189950
# RUN apt update && apt install -y texlive-font-utils zip unzip inkscape \
#   python3-pygments python3-pip

# # clone the tsx and jsx lexers repos (if you need to include tsx and jsx highlighted code in your PDF)
# RUN git clone https://github.com/cad0p/jsx-lexer
# RUN cd jsx-lexer && git checkout add-typescript && pip install -e .

# # or simply install the full version of TexLive
# # https://hub.docker.com/r/texlive/texlive
# FROM texlive/texlive:latest
