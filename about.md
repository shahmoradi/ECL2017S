---
layout: page
permalink: /about/index.html
# title: ECL-2017S
tags: [Amir, Shahmoradi, Instructor]
imagefeature: cover3.jpg
chart: true
---

{% assign total_words = 0 %}
{% assign total_readtime = 0 %}
{% assign featuredcount = 0 %}
{% assign statuscount = 0 %}

{% for post in site.posts %}
    {% assign post_words = post.content | strip_html | number_of_words %}
    {% assign readtime = post_words | append: '.0' | divided_by:200 %}
    {% assign total_words = total_words | plus: post_words %}
    {% assign total_readtime = total_readtime | plus: readtime %}
    {% if post.featured %}
    {% assign featuredcount = featuredcount | plus: 1 %}
    {% endif %}
{% endfor %}

<br>

## About ECL Course

Engineering Computation Lab (COE111L) is new course that is offered in the [department of Aerospace Engineering and Engineering Mechanics](http://www.ae.utexas.edu/){:target="_blank"} at the [University of Texas at Austin](http://www.utexas.edu/){:target="_blank"}, starting Spring 2017. The overarching goal of the course is to introduce Aerospace undergraduate students with the principles of scientific computing, as well as the applications of numerical methods that the students learn in Engineering Computation (ASE 211K), offered parallel to this course. Towards this goal, Python was chosen as default programming language of this course for the first offering of this, but can be switched to other languages such as R, MATLAB, Fortran, C++, or other languages in future, depending on the needs of Aerospace program at UT Austin.

### Syllabus
More information and details about the course content and class format can be found in the course [syllabus (PDF)](../Syllabus-COE111L.pdf){:target="_blank"}.

## About ECL Instructor

Dr. Amir Shahmoradi is a physicist by training and science-lover in general, with extensive teaching & research experience and background in high energy physics, astronomy and astrophysics, theoretical physics, statistics, data analysis and modeling, computational physics, Molecular Dynamics simulations, stochastic processes, Monte Carlo Methods, Bayesian probability theory, biomedical sciences and MRI data analysis, bioinformatics and evolutionary biology, in particular, viral evolution, protein dynamics and interactions.

<figure>
  <img src="{{ site.url }}/images/about/AmirShahmoradi300.png" alt="Instructor: Amir Shahmoradi">
  <figcaption>Instructor: Amir Shahmoradi</figcaption>
</figure>

## About ECL Students

As of {{ site.time | date: "%A, %d %b %Y" }} at {{ site.time | date: "%I:%M %p" }}, there are 19 Aerospace undergraduate students enrolled in this course. Below is the latest depiction of the students!

<figure>
	<img src="{{ site.url }}/images/about/minions.jpg" alt="students">
	<figcaption>The Spring 2017 class participants</figcaption>
</figure>

*[MRI]: Magnetic Resonance Imaging
*[UT Austin]: University of Texas at Austin

<br>

<div align="center"> <h2> UT Austin Campus Photos </h2> </div>

<figure class="third">
	<a href="{{ site.url }}/images/about/UTtowerSouthFaceEve.png"><img src="{{ site.url }}/images/about/UTtowerSouthFaceEve.png"></a>
	<a href="{{ site.url }}/images/about/UTtowerSouthFace.png"><img src="{{ site.url }}/images/about/UTtowerSouthFace.png"></a>
	<a href="{{ site.url }}/images/about/UTtowerNorthFace.png"><img src="{{ site.url }}/images/about/UTtowerNorthFace.png"></a>
</figure>
<figure class="half">
	<a href="{{ site.url }}/images/about/FacultyLoungeICES.png"><img src="{{ site.url }}/images/about/FacultyLoungeICES.png"></a>
	<a href="{{ site.url }}/images/about/chemistry.png"><img src="{{ site.url }}/images/about/chemistry.png"></a>
	<a href="{{ site.url }}/images/about/RLM.png"><img src="{{ site.url }}/images/about/RLM.png"></a>
	<a href="{{ site.url }}/images/about/UTtowerSouthFacePanoramic.png"><img src="{{ site.url }}/images/about/UTtowerSouthFacePanoramic.png"></a>
</figure>