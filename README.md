# End-to-End Data Pipeline with Azure Databricks and Power BI

Tämä projekti demonstroi modernin datan käsittelyputken rakentamista Azure-pilvipalveluilla. Projekti kattaa datan inkrementaalisen latauksen, puhdistuksen **Medallion-arkkitehtuurin** mukaisesti ja lopputulosten visualisoinnin Power BI:llä.

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

## Projektin rakenne

```plaintext
.
├── /architecture/           # Arkkitehtuurikaaviot (Mermaid)
├── /databricks_notebooks/   # Databricks-koodit (01-99)
├── /powerbi_report/         # Power BI -raporttimalli (.pbit)
└── README.md                # Tämä tiedosto
