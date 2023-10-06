**Installation av Python och Selenium:**

1. Ladda ner python 3.11.5 via följande länk <https://www.python.org/downloads/> vid installation klicka i rutan som lägger till python i path

![](/md-images/Bild2.png)

2. Ladda ner Visual Studio Code

![](/md-images/Bild3.png)

3. Ladda ner Python extension i Visual Studio Code

![](/md-images/Bild4.png)

4. Installera sedan Selenium genom att öppna cmd och skriva “py -m pip install selenium”

![](/md-images/Bild1.png)

**Installation av Node 18.17.1**

<https://nodejs.org/en>

**Installation av bootstrap och sass compiling**

<https://getbootstrap.com/docs/5.3/getting-started/download/#npm>

<https://getbootstrap.com/docs/5.3/customize/sass/#compiling>

**TypeScript**

För att ladda ner:

    npm install -g typescript

För att kompilera TS-kod:

    tsc [typescript-fil] --outDir ./js/ -t ES2016

\*Ersätt "\[typescript-fil]" med en path till TS-filen som ska kompileras

Du kan göra så att den auto kompilerar on save genom att kolla på den här videon <https://www.youtube.com/watch?v=VRT7M6PZDlw> om du får error “cannot be loaded because running scripts is disabled on this system.” Så ska du öppna powershell som admin och skriv in “Set-ExecutionPolicy RemoteSigned” och sedan “Y” för yes.

**Visual Studio extensions**

Hitta extensions i VSCode genom View -> Extensions eller Ctrl + Shift + X

**Black Formatter**

1. Ladda ner Black Formatter

\***\*![](/md-images/bf.png)\*\***

2. Öppna en python fil
3. Högerklicka på en tom yta och välj Format Document With…

![](/md-images/Bild5.png)  
4. Välj configure default formatter.  
5. Välj Black Formatter.  
6. Sök User Settings i Ctrl + Shift + P

![](/md-images/Bild6.png)

7. Sök format i sökrutan och klicka i rutan för Format On Save

![](/md-images/Bild7.png)

**Pylint:**

1. Ladda ner Pylint v2023.6.0

![](/md-images/Bild8.png)

2. Sök User Settings i Ctrl + Shift + P och välj JSON

![](/md-images/Bild9.png)

<!---->

3. Lägg till inställning för att ignorera fel (för att välja vilka fel som ignoreras ändra c0111) på följande sätt:

![](/md-images/Bild10.png)

**isort:**

![](/md-images/Bild11.png)

1. Ladda ner isort
2. Tryck ctrl shift p och sök open user setting.json
3. Lägg till denna kod under Black Formatter

<!---->

           "editor.codeActionsOnSave": {
                "source.organizeImports": true
            }

4. Se till så att filen nu ser ut så här

![](/md-images/Bild12.png)
