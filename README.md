# U.S. CMS Price Transparency: How can APIs help?

Use this project to discuss issues or develop tools/utilities to foster the establishment of APIs and best practices supporting efforts by the U.S. [Center Medicaid and Medicare Services](https://www.cms.gov/) to increase healthcare costs transparency, specifically [Hospital Price Transparency](https://www.cms.gov/hospital-price-transparency) and [Transparency in Coverage](https://www.cms.gov/healthplan-price-transparency) requirements. This repository complement our [Postman public workspace](https://go.postman.co/workspace/7d431065-785e-44f5-b70a-49ce1f8f9a63) on the topic, which the Postman Open Technologies team recently began to investigate as outlined in this [blog story](#).

## Data Sources

One of the first challenge we are facing is to actually find the data files, as there is no directory of reporting hospitals or insurance carriers. Establishing API driven registration mechanisms would help creating and maintaining such database. In the meantime, we can gather more information and links here.

### Hospitals

- [DoltHub Hospital Price Transparency database](https://www.dolthub.com/repositories/dolthub/hospital-price-transparency) - contains links and information for 1400 hospitals

### Coverage

Below links to web pages where data files from various carriers can be found (do add if you find more). Most websites present this information in different ways, and these resources are unfortunately not easy to harvest. In-network files can be extremely large, making them unpractical to read. Having standard API specifications and implementations providing access to this information in more useful ways (rather that data dumps) would greatly improve machine actionability and transparency. This would also facilitate implementation of pricing comparison tools required for phase two and three in 2023 and 2024.

- [Aetna](https://health1.aetna.com/app/public/#/one/insurerCode=AETNACVS_I&brandCode=ALICFI/machine-readable-transparency-in-coverage)
- [Cigna](https://www.cigna.com/legal/compliance/machine-readable-files)
- [Dean Health Plan](https://www.deancare.com/Helpful-Links/Transparency-in-coverage)
- [Dean / Prevea360 Health Plan](https://www.prevea360.com/Legal/Transparency-in-coverage)
- [Geisinger Health Plan](https://www.geisinger.org/health-plan/nosurprisesact)
- [Health Net](https://www.centene.com/price-transparency-files.html) (Ambetter, QualChoice, Health Net, MHN, WellCare of North Carolina, Fidelis)
- [Hawai'i Medical Service Association (HMSA)](https://www.centene.com/price-transparency-files.html)
- [Independence Blue Cross Blue Shield](https://www.ibx.com/developer-resources)
- [Kaiser Permanente](https://healthy.kaiserpermanente.org/front-door/machine-readable)
- [Medical Card Systems (MCS)](https://mcs.com.pr/es/Paginas/Transparency-es.aspx)
- [Medical Mutual](https://www.medmutual.com/For-Employers/Employer-Resources/No-Surprises-Act-Legislation.aspx)
- [Priority Health](https://www.priorityhealth.com/landing/transparency)
- [University of Pittsburgh Medical Center (UPMC)](https://www.upmchealthplan.com/transparency-in-coverage/mrf/)
- [Optum](https://transparency-in-coverage.optum.com/)
- [United Health](https://transparency-in-coverage.uhc.com/)

## Resources

### Stories

- [I analyzed 1835 hospital price lists so you didn't have to](https://www.dolthub.com/blog/2022-07-01-hospitals-compliance/), Alex Stein (DoltHub), 2022-07-01
- [Health-Insurance Providers Begin Publishing Prices for Medical Care](https://www.wsj.com/articles/health-insurance-providers-begin-publishing-prices-for-medical-care-11656685249), Wall Street Journal, 2022-07-01
- [Semi-Annual Hospital Price Transparency Compliance Report](https://www.patientrightsadvocate.org/semi-annual-compliance-report-2022), Patient Right Advocate.org, 2022-02
 
### CMS

- Medicare and Medicaid Programs: [CY 2020 Hospital Outpatient PPS Policy Changes and Payment Rates and Ambulatory Surgical Center Payment System Policy Changes and Payment Rates. Price Transparency Requirements for Hospitals To Make Standard Charges Public]() ([84 FR 65524](https://www.govinfo.gov/content/pkg/FR-2019-11-27/pdf/2019-24931.pdf))
- [Hospital Price Transparency resources](https://www.cms.gov/hospital-price-transparency/resources)
- [Transparency in Coverage: technical implementation guidelines](https://github.com/CMSgov/price-transparency-guide) for the machine readable files. This GitHub repository provides access to JSON/XML schema
- [Transparency in Coverage](https://www.federalregister.gov/documents/2019/11/27/2019-25011/transparency-in-coverage) final rules ([85 FR 72158](https://www.govinfo.gov/app/details/FR-2020-11-12/2020-24591)).















