#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False
"""

Biologically-inspired characterization of sparseness in natural images

"""
import os
home = os.environ['HOME']

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

meta = dict(
 embed = True,
 draft = DEBUG, # show notes etc 
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 #reveal_path = 'file://' + home + '/pool/libs/numbers/ipython_slides/reveal.js/',
 reveal_path = 'http://cdn.jsdelivr.net/reveal.js/3.0.0/',
 #reveal_path = 'https://s3.amazonaws.com/hakim-static/reveal-js',
 theme='night',
 author='Laurent U Perrinet (INT)',
 author_link='<a href="http://invibe.net">Laurent U Perrinet (INT)</a>',
 title="""Biologically-inspired characterization of sparseness in natural images""",
 short_title='Biologically-inspired characterization of sparseness in natural images',
 conference='<a href="http://invibe.net/LaurentPerrinet/Presentations/2016-10-26_EUVIP_BICV">EUVIP Special Session on BICV</a>, Wednesday, October 26, 2016',
 Acknowledgements="""<h3>Acknowledgements:</h3>
         <ul>
             <li>Jim Bednar @ Continuum Analytics &amp; University of Edinburgh</li>
             <li>Wahiba Taouali, Giacomo Benvenuti, Frédéric Chavane</li>
             <li>Pascal Wallisch and Tony Movshon @ NYU for the MT data</li>
             <li>Rick Adams and Karl Friston @ UCL</li>
             <li>Mina Aliakbari Khoei, Guillaume Masson and Anna Montagnini for the psychophysics</li>
        </ul>
""",
#     <li>Wahiba Taouali, Giacomo Benvenuti, Frédéric Chavane - ANR BalaV1 </li>
 abstract="""
""",
 sections= ['Priors in natural images',
    'Quantification of sparseness in natural images',
    'Perspectives: neurophysiology']
 )
do_section = [True] * (len(meta['sections']) + 2)
i_section = 0
s = Slides(meta)
if do_section[i_section]:
 s.open_section()
 #################################################################################
 ## Intro - 5''
 #################################################################################
 #################################################################################
 figpath = os.path.join(home,   'pool/libs/numbers/ipython_slides/slides.py/figures/')
 s.hide_slide(content=s.content_figures(
   [os.path.join(figpath, 'mire.png')], bgcolor="black",
   height=s.meta['height']),
       notes="""
Check-list:
-----------

* (before) bring miniDVI adaptors, AC plug, remote, pointer
* (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
* (VP) open monitor preferences / calibrate / title page
* (timer) start up timer
* (look) @ audience

Preparing Effective Presentations
---------------------------------

Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.

Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.

Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.

Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.

Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.

Unified - An image is most effective when information is organized around a single central theme and tells a unified story.

Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.

Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.

Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.

Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.

Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.

Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.

Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.

http://pne.people.si.umich.edu/PDF/howtotalk.pdf

 """)
 intro = """
 <h2 class="title">{title}</h2>
 <h3>{author_link}</h3>
 """.format(**meta)
 intro += s.content_figures(
    [os.path.join(figpath, "troislogos.png")], bgcolor="black",
   height=s.meta['height']*.3, width=s.meta['height']*1.2)
 intro += """
 {Acknowledgements}
 <h3>{conference}</h3>
   """.format(**meta)
 s.add_slide(content=intro,
    notes="""
* (AUTHOR) Hi, I am Laurent Perrinet from (LOGO) the Institute de Neurosciences de la Timone in Marseille, a joint unit from the CNRS and AMU. Using computational models, I am investigating the link between the efficiency of behavioural responses in vision, their underlying neural code and their adaptation to the structure of the world.

* (SHOW TITLE - THEME) = In particular, eye movements, that is, motion of the eyeballs targeted at orienting our gaze in the visual field, provide a large repertoire of behaviors at different time scales from fast, reflexive-like saccades to smooth movememnts and even to long-term adaptation.

* (SHOW TITLE -OBJECTIVE) today, I will be focusing on the key challenges in modelizing visually guided eye movements and more generally to better understand decision making in biology (the living kingdom).  in particular, we will focus on the dynamics of these mechanisms to unravel the sequence of processes which allow the efficient response of motor commands to the environment. As such, my goal here is to show that the solutions proposed by motion perception and EMs provide a generic (and rather unique) framework to finesse models of decision making in the generic theory championned by Karl Friston, active inference (AI)

* (ACKNO) this endeavour involves different techniques, tools and... persons. From the head on, I wish to thank the people who collaborated to this project and in particular Rick Adams and Karl Friston and the Wellcome Trust Centre for Neuroimaging for providing the tools for a successful visit / but also Mina, Guillaume and Anna for the great oppportunity to link  theories with psychophysical data; Wahiba, Giacomo and Frédéric for the challenging task of linking such models to the neural activity in NHP, and finally Jean-Bernard, Sohir and Laurent Madelain for their essential knowledge in adaptation and reinforcement.

more precisely... what are eye movements and how can they be useful for active inference?

 """)



# open questions:
figpath = os.path.join(home, 'science/CNRS/2016-07-07_EDP-proba/figures')
figpath = os.path.join(home, 'quantic/RTC/2016-04-01_biomimétique/figures')
for fname in [
             'Dynamo-on.jpg',
             'Dynamo-off.jpg',
             # 'optical-illusions-part-2-63.jpg', # room
              #'funny-perfectly-timed-photos-17__700.jpg', # au luxembourg
              'prior-optical-illusions-part-2-68.jpg', # face
              'power.png', # lee sedol
              ]:
    s.add_slide(content=s.content_figures(
      [os.path.join(figpath, fname)], bgcolor="black",
      height=s.meta['height']*.99),
      #image_fname=os.path.join(figpath, fname),
                      notes="""
it is the set of cognitive processes that allow to make sense from the visual inputs

- illusions visuelles:  Anamorphose par Felice Varini Felice Varini "vingt-trois disques évidés plus douze moitiés et quatre quarts" Exposition:
"DYNAMO" Grand Palais, Paris 2013 Photo: André Morin
- on peut apprendre rapidement qu'il ne faut pas croire tout ce qu'on voit
(surtout si c'est sur internet)

- power.png = efficacité

- priors

""")
figpath = os.path.join(home, 'quantic/science/2016-01-XX_PerrinetBednar15/talk')
# visual
s.add_slide(#image_fname=os.path.join(figpath, 'p4100011.jpg'),
            content=s.content_figures(
              [os.path.join(figpath, 'p4100011.jpg')], bgcolor="black",
              height=s.meta['height']*.99),
                      notes="""
... by linking to the statistics of natural images:

* (natural) For instance, oriented edges that constitute images of natural scenes
tend to be aligned in co-linear or co-circular arrangements, such as when
💠 you follow the contours of these boulders: lines and smooth curves
are more common than other possible arrangements of edges. See for example
the work of Mariano Sigman on co-circularity in natural images (see Sigman, 2001).

* (neural) The visual system appears to take advantage of this prior
information, and human contour detection and grouping performance is well
predicted by what is coined an "association field" (Field et al., 1993)...
""")

s.close_section()
#####################################################################################
## AssoField - 15''
#####################################################################################
#####################################################################################
s.open_section()
s.add_slide_outline(1)
figpath = os.path.join(home, 'quantic/science/2016-01-XX_PerrinetBednar15/talk')
for fname in [
            'scheme_thorpe.jpg',
            #'PerrinetBednar13-figure1A.jpg',
            'loggabor.png',
             'fig_architecture.png',

              ]:
    s.add_slide(content=s.content_figures(
          [os.path.join(figpath, fname)], bgcolor="black",
          title=None, height=s.meta['height']*.95)+
          s.content_bib("LP", "2015", 'Sparse models in <it>BICV</it>, <a href="http://github.com/bicv/SparseEdges">http://github.com/bicv/SparseEdges</a> <BR>'),
           notes="""


Methods:

# - LogGabor
	 in order to do that, we first used a linear transformation using a log-gabor representation
* (definition) this representation is a good and generic model of edges as defined by
 their shape, orientation and scale. It matches what is well described for the response of simple cells'
 response in area V1.  we show here on the top left that these filters tile evenly the Fourier space,
 but also that these correspond to a good model of edges at different orientation, scale and phase compared
 to other dictionaries like the Daubechies wavelet base Db4 in (e) and the steerable pyramid by Eero Simoncelli,
  \item[(Fischer) obviously, this dictionary is over-complete, but their correlation is easy to compute and
  allow for a relative translation-rotation-scale invariance. we proved that this was better adapted to the
  extraction of edges than gabors (Fischer, 07).

coupled with a sparse coding algorithm.

# - SparseEdges /Users/laurentperrinet/quantic/2015_RTC/2014-04-17_HDR/figures/v1_tiger.mp4

* (MP)  from this linear representation, we searched for the most sparse representation using a $\ell_0$ norm
approach for which Matching Pursuit proved to be  a good approximation. I refer to this paper that appeared
in IEEE TIP for more details [LP (2003) IEEE TIP, LP (2015) BICV] (BICV)] and that i reviewed in a recent book
chapter (Perrinet, 2015 bicv), including a model of complex cells' response (Fischer, 2007). It is generic and efficient.

We then computed the ``association field'' ...  ../ms/figure_model_ls.png}\\%
 - SVM
 github links

""")
import numpy as np
figpath = '.'
list_of_number_of_edge =  2* 4**np.arange(6)
experiment = 'EUVIP-sparseness'
name = experiment.replace('_sparseness', '_lena')
figpath, ext, dpi = '.', '.png', 600


for fname in [
            name + '_movie_N' + str(number_of_edge) + ext
            for number_of_edge in list_of_number_of_edge ]:
    s.add_slide(content=s.content_figures(
          [os.path.join(figpath, fname)], bgcolor="black",
          title=None, height=s.meta['height']*.95),
           notes="""


""")

for fname in [
            'EUVIP-sparseness_raw_inset.png',
            'EUVIP-sparseness_proba_inset.png',
              ]:
    s.add_slide(content=s.content_figures(
          [os.path.join(figpath, fname)], bgcolor="black",
          title=None, height=s.meta['height']*.95),
           notes="""


""")

s.close_section()
#####################################################################################
## AssoField - 15''
#####################################################################################
#####################################################################################
s.open_section()
s.add_slide_outline(2)
figpath = os.path.join(home, 'pool/science/RetinaClouds/2016-01-12_trajectory-kick-off/figures/')

for fname in [
            '20151113-135529-20151113_135529.jpg',
            '20151113-135940-20151113_135940.jpg',
              ]:
    s.add_slide(content=s.content_figures(
          [os.path.join(figpath, fname)], bgcolor="black",
          title=None, height=s.meta['height']*.95),
           notes="""


""")
figpath = os.path.join(home, 'pool/science/RetinaClouds/2016-09-14_droplets_round2/data_cache/2016-09-14_frames/')

s.add_slide(content="""
    <video controls autoplay loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath, '00003_droplets_i_sparse_0_seed_1974.mp4'))),
    notes="""

""")

for figpath, fname in [
    (os.path.join(home, 'pool/science/RetinaClouds/2016-01-12_trajectory-kick-off/figures/'),
    'droplets_raster.png'),
    (os.path.join(home, 'pool/science/RetinaClouds/2016-05-20_nips/'),
    'STA.png'),
      ]:
    s.add_slide(content=s.content_figures(
          [os.path.join(figpath, fname)], bgcolor="black",
          title=None, height=s.meta['height']*.95),
           notes="""


""")
s.close_section()

s.add_slide_outline()
s.add_slide(content=intro,
    notes="""
Thanks for you attention!
""")

s.compile(filename='2016-10-26_Perrinet16EUVIP_talk.html')
