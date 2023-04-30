# U.S. CMS Price Transparency: How can APIs help?

Use this project to discuss issues or develop tools/utilities to foster the establishment of APIs and best practices supporting efforts by the U.S. [Center Medicaid and Medicare Services](https://www.cms.gov/) to increase healthcare costs transparency, specifically [Hospital Price Transparency](https://www.cms.gov/hospital-price-transparency) and [Transparency in Coverage](https://www.cms.gov/healthplan-price-transparency) requirements. This repository complement our [Postman public workspace](https://www.postman.com/postman/workspace/postman-open-technologies-u-s-cms-transparency-in-coverage/overview) on the topic, which the Postman Open Technologies team recently began to investigate as outlined in this [blog story](#).

## Data Sources

One of the first challenge we are facing is to actually find the data files, as there is no directory of reporting hospitals or insurance carriers. Establishing API driven registration mechanisms would help creating and maintaining such database. In the meantime, we can gather more information and links here.

### Hospitals

- [DoltHub Hospital Price Transparency database](https://www.dolthub.com/repositories/dolthub/hospital-price-transparency) - contains links and information for 1400 hospitals

### Coverage

Consult this [Google spreadsheet](https://docs.google.com/spreadsheets/d/1Uuphuk41tFGmrulXhfeDN2zVkmVLzb4S1kdq20-4uZo/edit?usp=sharing) for links and information on websites we have identified where data can be found. Request edit access or file an issue if you wish to contribute. Most present this information in different ways, and these resources are unfortunately not easy to harvest. In-network files can be extremely large, making them unpractical to read. 

Having standard API specifications and implementations providing access to this information in more useful ways (rather that data dumps) would greatly improve machine actionability and transparency. This would also facilitate implementation of pricing comparison tools required for phase two and three in 2023 and 2024.

The following companies are developing solutions or readily offering access to the data in various ways. Contact them for further information.

- [Serif Health](https://www.serifhealth.com/)
- [Turquoise Health](https://turquoise.health/for_payers)

## Resources

### Stories

- [Health insurers just published close to a trillion hospital prices](https://www.dolthub.com/blog/2022-09-02-a-trillion-prices/), Alex Stein (DoltHub), 2022-08-01
- [APIs and Beyond: Conversation with Alec Stein](https://youtu.be/nJ1P84dQ4W0), Pascal Heus (Postman Open Technologies), 2022-08
- [Real-Time Payer Rates Data Tracker](https://blog.turquoise.health/turquoise-health-real-time-payer-rates-tracker/), Adam Geitgey / Chris Severn (Turquoise Health), 2022-07-15
- [I analyzed 1835 hospital price lists so you didn't have to](https://www.dolthub.com/blog/2022-07-01-hospitals-compliance/), Alex Stein (DoltHub), 2022-07-01
- [Health-Insurance Providers Begin Publishing Prices for Medical Care](https://www.wsj.com/articles/health-insurance-providers-begin-publishing-prices-for-medical-care-11656685249), Wall Street Journal, 2022-07-01
- [Semi-Annual Hospital Price Transparency Compliance Report](https://www.patientrightsadvocate.org/semi-annual-compliance-report-2022), Patient Right Advocate.org, 2022-02
 
### CMS

- Medicare and Medicaid Programs: [CY 2020 Hospital Outpatient PPS Policy Changes and Payment Rates and Ambulatory Surgical Center Payment System Policy Changes and Payment Rates. Price Transparency Requirements for Hospitals To Make Standard Charges Public]() ([84 FR 65524](https://www.govinfo.gov/content/pkg/FR-2019-11-27/pdf/2019-24931.pdf))
- [Hospital Price Transparency resources](https://www.cms.gov/hospital-price-transparency/resources)
- [Transparency in Coverage: technical implementation guidelines](https://github.com/CMSgov/price-transparency-guide) for the machine readable files. This GitHub repository provides access to JSON/XML schema
- [Transparency in Coverage](https://www.federalregister.gov/documents/2019/11/27/2019-25011/transparency-in-coverage) final rules ([85 FR 72158](https://www.govinfo.gov/app/details/FR-2020-11-12/2020-24591)).















