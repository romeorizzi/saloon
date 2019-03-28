# Saloon: Wednesday, cope without the keys: `6`, `7`, `8`, and `0`

## General setting of the sequel (this is episode 3 of a sequel of 7 problems):

You have a part-time job in a saloon.
The job is flexible and asks you to play the piano, clean the floor (which is where you actually get your reward for the job), but also to mantain the records of the bills. Every time a customer exits the saloon, you must annotate his unpayed dues. 
At a certain point of your working day your recording might look somethink like:

```23, 5, 1, 1, 57, 12,```

that is, before every comma comes a positive natural number written in decimal notation. At the beginning of the day the recording is empty (no comma) and during the day you append new numbers (each followed by a comma) at the right end of the previous recording. You can think customers exit the saloon one by one and you simply add the required typewriter keystroke in order to add the new unpaid amount at the end of the record. The point is being able to faithfully reconstruct the sequence.

You live in a small village and the customers of the saloon are a quite colorful gang, sometimes they quarrel and end up having to pay for the mess with no mony in their pockets, this is what originally opened the tradition of keeping the bills annotated. This is also necessary in many other situations (drunk too much beer or whisky, holding a gun bigger than that of the sceriff, lost everything at the card table, got seriously wunded in a shooting, ...).
The frequent shootings do not scare you in that, as we said, you are also the one who plays the piano. They do affect your recording activity however in that, while initially you had the ten digits plus a comma key on your typewriter keyboard, it so happens that in the traditional evening shootings at the saloon some keys of the typewriter get broken and, the day after, you must organize yourself to cope with those keys which are left.


### Goals 

Questo secondo problema del sequel già ti chiede di gestirtela con un tasto in meno. Comincia quindi a farsi divertente.
Anche questa volta devi implementare le seguenti funzioni, la vera differenza essendo che ora non puoi più utilizzare il carattere '6' per la scrittura dei numeri della sequenza:

```get_original_string(string_length, string_over_alphabet_0123456789comma)```: in questa procedura dovrai riportare le informazioni, eventualmente opportunamente elaborate, dentro una variabile globale che ti consenta di rispondere alle domande poste tramite le due funzioni successive. 


```tell_encoding_string_length()```:
    ritorna la lunghezza della stringa da tè scritta per tenere traccia della stringa che avresti scritto qualora in possesso di tutti e 11 i tasti di fabbrica della tua macchina da scrivere.

```tell_encoding_string_ith_char(i)```:
    ritorna l'i-esimo carattere della stringa da tè scritta. Questa stringa non potrà contenere caratteri di tasti che sono andati persi. 

```get_encoded_string(string_length, string_over_reduced_alphabet)```:
   Quando TuringArena chiama questa funzione il processo in cui sono state chiamate le funzioni precedenti è già stato chiuso, e pertanto non trovi più nulla nelle tue variabili globali.
   Questa funzione ti riconsegna la stringa da tè impressa sul foglio nella tua macchina da scrivere. Le due successive funzioni verificano la tua capacità di ricostruire la stringa originale partendo da questa tua rappresentazione della stessa. Di nuovo, quantomeno se qualche tasto è andato perso, ti converrà effettuare entro questa procedura le tue elaborazioni, ed in ogni caso predisporre dentro opportune variabili globali le risposte già sostanzialmente pronte che le due seguenti funzioni dovranno fornire.
   
```tell_original_string_length()```: facile da implementare se hai precedentemente (in funzione immediatamente precedente) ricostruito la stringa originale e la hai salvata in una variabile globale. 

def tell_original_string_ith_char(i): facile da implementare se hai precedentemente (in funzione immediatamente precedente) ricostruito la stringa originale e la hai salvata in una variabile globale.

I problemi di questa saga ti richiedono, quando qualche tasto è andato perso, di escogitare meccanismi attraverso i quali codificare e decodificare le informazioni.
Il primo goal che devi porti è quello di essere sempre in grado di decodificare quanto da tè codificato. 
Poi possiamo chiederti di farlo con efficienza. Per efficienza intendiamo che la quantità di inchiostro che vai a consumare non cresca troppo rispetto alla quantità di inchistro che avresti utilizzato potendoti avvalere dei tuoi 11 tasti (10 cifre più la virgola) nella dotazione standar.
Vorresti ad esempio minimizzare quella costante C per cui poter dire che il numero di keystrokes impiegato è sempre al più C volte il numero di keystrokes che avresti impiegato con la macchina in dotazione originale.
Formulata in modo più preciso,
dove si indichi con `used` il numero di keystrokes che impieghi e con `got` la lunghezza del record rappresentato,
cerca di minimizzare quella costante C per cui:

```used <= C got + 3```

Nella versione attuale ti teniamo sotto osservazione i seguenti goals (se ce ne suggerisci altri cercheremo di supportare anche quelli):

- `correct`
- `correct_C_is_2`
- `correct_C_is_1dot5`


## In this episode:

Yesterday evening was a big mess, the seriff accused the Dalton to be the ones who enterd the saloon last night to solo key numeber `6`, and there was a huge fight.
In the mess, besides key `6`, also the following keys have gone broken:
`7`, `8`, and `0`.
The whole village hopes the saloon can remain open. Can you keep hold at your work?
To contribute to your mission, the Dalton and the serfiff have given you some extra ink for typewriters. 
If you see the description of the goals, you see you have more availability now. 

