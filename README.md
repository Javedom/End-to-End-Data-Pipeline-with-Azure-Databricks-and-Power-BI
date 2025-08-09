# End-to-End-Data-Pipeline-with-Azure-Databricks-and-Power-BI
Tämä projekti demonstroi modernin datan käsittelyputken rakentamista Azure-pilvipalveluilla. Projekti kattaa datan inkrementaalisen latauksen, puhdistuksen Medallion-arkkitehtuurin mukaisesti, ja lopputulosten visualisoinnin Power BI:llä.


graph LR
    subgraph "Azure Cloud"
        subgraph "Storage (ADLS Gen2)"
            A[fa:fa-file-csv Raw CSV Files<br/>/raw] --> B
            direction LR
        end

        subgraph "Compute & Governance (Databricks)"
            B(fa:fa-cogs<br/><b>Autoloader</b><br/>Incremental Ingest) --> C[fa:fa-database<br><b>Bronze Layer</b><br>Delta Table<br>/bronze]
            C --> D{fa:fa-magic<br>Transform<br>& Clean}
            D --> E[fa:fa-database<br><b>Silver Layer</b><br>Cleansed Delta<br>/silver]
            E --> F{fa:fa-calculator<br>Aggregate<br>& Business Logic}
            F --> G[fa:fa-star<br><b>Gold Layer</b><br>Aggregated Marts<br>/gold]
            
            subgraph "Management Plane"
                direction TB
                H(fa:fa-lock<br><b>Unity Catalog</b><br>Governance<br>Security)
                I(fa:fa-calendar<br><b>Databricks Jobs</b><br>Orchestration)
            end
        end
    end

    subgraph "BI & Reporting"
        J[fa:fa-bar-chart<br><b>Power BI</b><br>Dashboard & KPIs]
    end

    %% --- Connections ---
    G -- SQL Warehouse --> J
    I --> B
    H -- Manages Access --> B
    H -- Manages Access --> C
    H -- Manages Access --> E
    H -- Manages Access --> G
