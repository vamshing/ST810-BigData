## A Predictive Model to estimate subject's musical ability based on brain activity data.
**Author:** Guduguntla Vamshi
  affiliation:North Carolina State University, Raleigh , NC
  email: gudugu@ncsu.edu
date: January 2014

**Abstract:** The aim of this paper is to develop a Statistical model to predict te musical ability of an individual subject. We are given a data-set which contains the response of 200 subjects at different locations in the brain space. The space forms a 3D area with (u,v,w) spanning voxels in the brain. The predictive model proposed, uses a form of penalized-regression called Group Lasso Technique. The brain voxels are grouped together using a novel method called, the pointindex estimation, which groups the brain hot-spots together in producing the response.The results are compared with Ordinary Least Squares and Ridge Regression, the current standard methods of penalized regression to demonstrate the efficacy of the proposed model.


### Introduction
This paper is produced as a partial requirement of the course ST 810: Big Data by Dr.Reich at Statistics Dept.,NCSU. The data-set consistis of predictor variables which record the brain response to test the musical ability. The dimensional space of the brain {u,v,w} is uniformly mapped accross 20x20x20 space, producing 8,000 voxels in the region for an individual subject.With n=100, the total number of subjects, the data-set has the musical ability index as the response variable.

# Theory
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# Conclusion
Right now, your options for formatting bibliographies using Pandoc are to offload the work to biblatex (or natbib), or have pandoc handle everything via `citeproc` and CSL files. The latter way is simpler and cleaner, especially if we want to preserve the ability to easily generate both HTML and LaTeX/PDF outputs. You have to do two things. First, explicitly specify the "References" header. Second, pandoc does not (yet) support some standard layout options for bibliography entries---it will treat each entry like a regular paragraph, when we want the first lines of each bibliography entry to have no indentation, with subsequent lines (if any) to hang in from the margin. The LaTeX commands below the "References" header accomplish this . The LaTeX commands are ignored when HTML is produced, and do not show up in the output file.

# References
\setlength{\parindent}{-0.2in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{8pt}
\vspace*{-0.2in}
\noindent
