# End-to-End Data Pipeline: Azure Databricks ja Power BI

Tämä projekti demonstroi datakäsittelyputken rakentamista Azure-pilvipalveluilla. Projekti kattaa datan (inkrementaalisen) latauksen, puhdistuksen **Medallion-arkkitehtuurin** mukaisesti ja lopputulosten visualisoinnin Power BI:llä.

Projektin ytimessä ovat **Azure Databricks**, **Delta Lake** ja **Unity Catalog**, jotka yhdessä muodostavat skaalautuvan, luotettavan ja hallitun data-alustan.

---

## Arkkitehtuuri

Projekti noudattaa vaiheittaista datan jalostusmallia (**Medallion-arkkitehtuuri**), joka varmistaa datan laadun ja käytettävyyden eri tarpeisiin.

1. **Lähdedata:**  
   CSV-muotoiset raakatiedostot saapuvat **Azure Data Lake Storage (ADLS) Gen2** -tallennustilille.

2. **Datan ingestointi (Bronze):**  
   Databricks **Autoloader** tunnistaa uudet tiedostot automaattisesti ja lataa ne tehokkaasti ja inkrementaalisesti Bronze-tason Delta-tauluun. Data tallennetaan tässä vaiheessa alkuperäisessä muodossaan.

3. **Datan puhdistus (Silver):**  
   Bronze-tason dataa puhdistetaan ja muunnetaan: tietotyypit korjataan, duplikaatit poistetaan ja data rikastetaan. Lopputuloksena on luotettava ja yhtenäinen Silver-tason Delta-taulu.

4. **Datan aggregointi (Gold):**  
   Silver-tason datasta luodaan liiketoimintaa varten aggregoituja ja optimoituja Gold-tason tauluja (fakta- ja dimensiotaulut), jotka ovat valmiita analysoitavaksi.

5. **Orkestrointi ja laadunvalvonta:**  
   Koko putki (Bronze → Silver → Gold) on automatisoitu yhtenäiseksi prosessiksi **Databricks Jobs** -työkalulla. Jokaisen ajon lopuksi suoritetaan *data quality* -testit varmistamaan lopputuloksen laatu.

6. **Hallinnointi ja tietoturva:**  
   **Unity Catalog** toimii keskitettynä kerroksena, joka hallinnoi kaikkien data-assettien metatietoja, käyttöoikeuksia (*STORAGE CREDENTIALS*) ja fyysisiä sijainteja (*EXTERNAL LOCATIONS*).

7. **Raportointi ja visualisointi:**  
   Power BI yhdistyy suoraan **Databricks SQL Warehouseen** ja lukee dataa Gold-tason tauluista. Lopputuloksena on interaktiivinen dashboard keskeisistä KPI-mittareista.

---

## Tekninen toteutus

| Osa-alue               | Teknologia / Työkalu |
|------------------------|----------------------|
| **Pilvialusta**        | Microsoft Azure      |
| **Tietovarasto**       | Azure Data Lake Storage (ADLS) Gen2 |
| **Datan käsittely**    | Azure Databricks     |
| **Kielet**             | PySpark, SQL, DAX    |
| **Datan ingestointi**  | Autoloader           |
| **Arkkitehtuuri**      | Medallion (Bronze, Silver, Gold) |
| **Tiedostomuoto**      | Delta Lake (ACID-transaktiot) |
| **Hallinnointi**       | Unity Catalog        |
| **Orkestrointi**       | Databricks Jobs      |
| **Laadunvarmistus**    | Assert-lauseet, notebook-pohjaiset testit |
| **BI-työkalu**         | Power BI             |

---


## Oppeja

### Keskeiset opit

- **Metatiedon ja datan ero:**  
  Tärkeää on erottaa fyysiset datatiedostot ADLS:ssä ja niiden looginen esitysmuoto (taulu) Unity Catalogissa. `save()` ja `saveAsTable()` ero. PowerBI ei tunnistanut viimeistä Gold-taulua ja jäin joksikin aikaa jumiin tämän takia.

- **Unity Catalogin rooli:**  
  Ymmärrys siitä, miten Clusterin Access Mode, Storage Credentials ja External Locations toimivat yhdessä turvallisen ja hallitun tiedonhallinnan mahdollistamiseksi. Ylipäänsä näiden oikein konfiguroiminen vaati todella paljon aikaa, kun sen oli tehnyt kerran väärin.

- **Striimin ja eräajon ero:**  
  Jatkuvasti kuunteleva striimi eroaa kerta-ajosta( `.trigger(availableNow=True)`). Kun tein Databricks-Jobin, jäi ensimmäinen "Ingest"-osio looppaamaan eikä edennyt muihin Medallion-osioihin.
  
- **Python ja PySpark:**
   Tässä projektissa olisi ollut helpompi rakentaa Databricksin notebookit eli Medallion-vaiheet SQL:ää käyttäen. Python tuotti uutena kielenä hankaluuksia, mutta taitaa olla ketterämpi kun eri Pipelinejen kompleksisuus kasvaa.
  

---


