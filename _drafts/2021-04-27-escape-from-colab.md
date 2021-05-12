---
toc: true
layout: post
description: Eventually, you're going to want to to escape from the Colaboratory. Here is how to do it.
categories: [colaboratory, python]
title: Escape From Colab
---

# Escape From Colab

> Everybody loves free stuff
>
> Anon

Ask any budding Data Scientist what they want and, after answering coffee, 
you might hear:

> A GPU, maybe 2; actually, as many GPUs as you've got.

Sadly, not everyone has the budget to outbid the countless crypto-miners who 
are consistently driving up the price of anything capable of rapid 
number-crunching.

![](https://images.unsplash.com/photo-1587134160474-cd3c9a60a34a "A GPU is for life, not just for Christmas")

Just when all hope appears to be lost, enter Google Colaboratory.

> Colaboratory, or “Colab” for short, is a product from Google Research. Colab 
> allows anybody to write and
> execute arbitrary python code through the browser, and is especially well 
> suited to machine learning, data 
> analysis and education. More technically, Colab is a hosted Jupyter 
> notebook service that requires no setup 
> to use, while providing free access to computing resources including GPUs.
>
> [Google](https://research.google.com/colaboratory/faq.html)

Colab provides a platform where anyone can run experiments, train models and 
hone their skills in a free-to-access walled garden.

Now this walled garden is great for an out of the box solution. It works, 
it is (fairly) easy to use, and it very closely mirrors a 
[jupyter notebook](https://jupyter.org/).

However, the problem with the walled garden is that sooner or later you are 
going to want to jump the fence. And Google really don't make that easy.

Here are my hints and tips for bridging that gap and helping integrate 
Colab as a core component of your ML Toolkit.

# Persisting Data

Each time you load up a notebook in Colab it runs in its own temporary VM. 
This is great if you mess up and want to be able to start from scratch, but 
not so great if you want to persist anything, such as data.

Luckily, Google have implemented a package which allows you to easily connect 
to Google Drive, their cloud storage platform. By default, every user has 
access to 15GB of free storage across Gmail, Drive and Photos. 
Google lets you expand this to either 100GB or 200GB through their 
[One](https://one.google.com/storage) subscription plan.

When we're working with large volumes of data, 15GB of storage starts to 
fill up pretty quickly. Luckily, there are steps we can take to reduce 
our footprint and the size of our data at rest.



# Version Control

# Using Your Model

# Conclusion