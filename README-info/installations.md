**Installation av Python och Selenium:**

 

1. Ladda ner python 3.11.5 via följande länk <https://www.python.org/downloads/> vid installation klicka i rutan som lägger till python i path

 

![](/md-images/Bild2.png)

 

2. Ladda ner Visual Studio Code

 

![](/md-images/Bild3.png)

 

3. Ladda ner Python extension i Visual Studio Co

 

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

 

\*ersätt "\[typescript-fil]" med en path till TS-filen som ska kompileras

 

du kan göra så att den auto kompilerar on save genom att kolla på den här videon <https://www.youtube.com/watch?v=VRT7M6PZDlw> om du får error “cannot be loaded because running scripts is disabled on this system.” Så ska du öppna powershell som admin och skriv in “Set-ExecutionPolicy RemoteSigned” och sedan “Y” för yes.

 

**Visual studio extensions**

 

Hitta extensions i VSCode genom View -> Extensions eller Ctrl + Shift + X

 

**Blackformater**

 

1. Ladda ner Black Formatter

 

****![](/md-images/bf.png)****

 

2. Öppna en python fil
3. högerklicka på en tom yta och välj Format Document With…  

![](/md-images/Bild5.png)  
4. Välj configure default formatter.  
5. Välj Black Formatter.  
6. Sök User Settings i Ctrl + Shift + P

 

![](/md-images/Bild6.png)

 

7. Sök format i sökrutan och klicka i rutan för Format on save

 

![](/md-images/Bild7.png)

 

**Pylint:**

 

1. Ladda ner Pylint v2023.6.0

 

![](/md-images/Bild8.png)

 

2. ![](/md-images/Bild9.png)Sök User Settings i Ctrl + Shift + P och välj JSON

 

<!---->

 

3. Lägg till inställning för att ignorera fel (för att välja vilka fel som ignoreras ändra c0111) på följande sätt:

 

![](/md-images/Bild10.png)

 

**isort**

 

1. Ladda ner isort ![](/md-images/Bild11.png)
2. Tryck ctrl shift p och sök open user setting.json
3. lägg till denna kod under black formatter

 

<!---->

 

           "editor.codeActionsOnSave": {
                "source.organizeImports": true
            }

 

4. se till så att filen nu ser ut såhär

 

![](/md-images/Bild12.png)

**Flask**  

Flask instalation guide
* https://www.youtube.com/watch?v=uxZuFm5tmhM&ab_channel=AmitThinks

**Azure**

 Skapa ett konto på microsoft Azure med ditt github student pack
 
 När du skapat ett konto klicka på create resource

![](/md-images/azure-img/azure1.png/)

Klicka på create under Web App

![](/md-images/azure-img/azure2.png/)

* Skapa en resource group

* Välj namn på sidan

* Under "puplish" välj code

* Under "runtime stack" välj Python - 3.11 

* Under "region" välj north europe

* Under "linux plan" välj B1 plan

* Sedan tryck "review + create"

![](/md-images/azure-img/azure3.png/)

Sedan efter laddning gå in på "go to resource" 

![](/md-images/azure-img/azure4.png/)

Här kommer din domain upp

![](/md-images/azure-img/azure5.png/)
### koppla Github och Azure

Ladda ned publish profile

![](/md-images/azure-img/azure6.png/)

* Öppna den nedladdade filen i vscode

* Kopiera allt i filen 

* Gå in på din github

* Klicka på "Settings"

![](/md-images/azure-img/azure7.png/)

* Klicka på "Actions"

![](/md-images/azure-img/azure8.png/)

* Skapa en "New repository secret"

![](/md-images/azure-img/azure9.png/)

* Skapa ett namn till din secret under "Name"
* Klistra in det du kopierade under "Secret"
* Klicka Sedan på "Add secret"

![](/md-images/azure-img/azure10.png/)

* Nu ska du gå in på vscode
* gå in i mappen .github\workflows och öppna din .yml fil

![](/md-images/azure-img/azure11.png/)

* Skriv in namnet på web-appen i (app-name: "")
* Skriv in namnet på din secret efter "secrets." i (publish-profile: ${{ secrets. }})

![](/md-images/azure-img/azure12.png/)

Nu så kommer din main repository att laddas upp på din web-app varje gång du pushar till main

