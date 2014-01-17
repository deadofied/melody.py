melody.py
=========

**melody.py** generates random 10-note [first species counterpoint](http://en.wikipedia.org/wiki/Counterpoint#First_species) melodies by first finding a random *cantus firmus* melody that matches a set of heuristics and then finding an appropriate counterpoint melody. A total of [16 heuristics](https://github.com/AlexNisnevich/melody.py/blob/master/melody.py#L81-L212) are used for each individual melody and [4 heuristics](https://github.com/AlexNisnevich/melody.py/blob/master/melody.py#L214-L239) are used to match two melodies in counterpoint. Results are outputted as MIDI files using Pyknon and then played using Timidity.

### Table of Contents

1\.  [Video Demonstration](#videodemonstration)  
2\.  [Installation](#installation)  
2.1\.  [Ubuntu / Debian](#ubuntu/debian)  
2.2\.  [Other](#other)  
3\.  [Heuristics Used](#heuristicsused)  
3.1\.  [For each individual melody](#foreachindividualmelody)  
3.2\.  [To match cantus firmus melody to first species melody](#tomatchcantusfirmusmelodytofirstspeciesmelody)  
4\.  [Wish List](#wishlist)  

<a name="videodemonstration"></a>

### 1\. Video Demonstration

[![Link to Youtube video](images/youtube/8cF6pfrD4RM.png)](http://www.youtube.com/watch?v=8cF6pfrD4RM)

<a name="installation"></a>

### 2\. Installation

<a name="ubuntu/debian"></a>

#### 2.1\. Ubuntu / Debian

```
sudo apt-get install python-pip timidity
pip install pyknon
```

<a name="other"></a>

#### 2.2\. Other

Install [Pyknon](http://kroger.github.com/pyknon/) and [Timidity](http://timidity.sourceforge.net/).

<a name="heuristicsused"></a>

### 3\. Heuristics Used

<a name="foreachindividualmelody"></a>

#### 3.1\. For each individual melody

Both the cantus firmus and the first species must satisfy the following rules:

1. No repeated notes in cantus firmus (one repetition allowed in first species).
2. No leaps that are an octave or larger.
3. No dissonant leaps.
4. Between two and four leaps in total.
5. Has a climax (highest note) that is not on the tonic or leading tone.
6. Changes direction at least two times.
7. No note repeated more than 3 times.
8. Final note approached by a step (not a leap).
9. Leaps larger than M3 must be followed by a change of direction.
10. The leading tone must always be followed by the tonic.
11. No more than two consecutive leaps in the same direction.
12. The same interval cannot occur twice in a row.
13. No noodling (that is, patterns such as N1 N2 N1 N2, for some notes N1 and N2).
14. No runs of more than four consecutive notes.
15. No unresolved melodic tension (that is, the start and end note of each run must be consonant together).
16. No repeated three-note patterns.

<a name="tomatchcantusfirmusmelodytofirstspeciesmelody"></a>

#### 3.2\. To match cantus firmus melody to first species melody

Together, the cantus firmus and the first species must satisfy the following:

1. No dissonant vertical intervals.
2. No vertical intervals larger than a 12th (P8 + P5).
3. No parallel fifths or octaves.
4. No parallel three-note chains.

<a name="wishlist"></a>

### 4\. Wish List

- support for other kinds of counterpoint
- support for melodies of other lengths (with rules tuned appropriately)
- web interface of some kind
- treating repeated notes as a single note of double duration rather than two separate notes
