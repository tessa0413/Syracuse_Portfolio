/****** Object:  Database UNKNOWN    Script Date: 11/13/2019 8:33:22 PM ******/

USE ist722_mafudge_oa5_dw
;

/* Drop table dbo.FactAccountBilling */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'dbo.FactAccountBilling') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE dbo.FactAccountBilling 
;
/* Drop table dbo.FactOrderDetails */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'dbo.FactOrderDetails') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE dbo.FactOrderDetails 
;
/* Drop table dbo.DimDate */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'dbo.DimDate') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE dbo.DimDate 
;

/* Create table dbo.DimDate */
CREATE TABLE dbo.DimDate (
   [DateKey]  int   NOT NULL
,  [Date]  date   NULL
,  [FullDateUSA]  nchar(11)   NOT NULL
,  [DayOfWeek]  tinyint   NOT NULL
,  [DayName]  nchar(10)   NOT NULL
,  [DayOfMonth]  tinyint   NOT NULL
,  [DayOfYear]  smallint   NOT NULL
,  [WeekOfYear]  tinyint   NOT NULL
,  [MonthName]  nchar(10)   NOT NULL
,  [MonthOfYear]  tinyint   NOT NULL
,  [Quarter]  tinyint   NOT NULL
,  [QuarterName]  nchar(10)   NOT NULL
,  [Year]  smallint   NOT NULL
,  [IsWeekday]  bit  DEFAULT 0 NOT NULL
, CONSTRAINT [PK_dbo.DimDate] PRIMARY KEY CLUSTERED 
( [DateKey] )
) ON [PRIMARY]
;



INSERT INTO dbo.DimDate (DateKey, Date, FullDateUSA, DayOfWeek, DayName, DayOfMonth, DayOfYear, WeekOfYear, MonthName, MonthOfYear, Quarter, QuarterName, Year, IsWeekday)
VALUES (-1, '', 'Unk date', 0, 'Unk date', 0, 0, 0, 'Unk month', 0, 0, 'Unk qtr', 0, 0)
;


/* Drop table dbo.DimProductPlan */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'dbo.DimProductPlan') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE dbo.DimProductPlan 
;

/* Create table dbo.DimProductPlan */
CREATE TABLE dbo.DimProductPlan (
   [ProdPlanKey]  int IDENTITY  NOT NULL
,  [ProdPlan_ID]  int   NOT NULL
,  [ProdPlan_Name]  varchar(50)   NOT NULL
,  [Department_Name]  varchar(20)   NOT NULL
,  [Price]  money   NOT NULL
,  [Source]  varchar(50)   NULL
,  [RowIsCurrent]  nchar(1)   NOT NULL
,  [RowStartDate]  datetime DEFAULT '01/01/1970'   NOT NULL
,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
,  [RowChangeReason]  nvarchar(200)    NULL
, CONSTRAINT [PK_dbo.DimProductPlan] PRIMARY KEY CLUSTERED 
( [ProdPlanKey] )
) ON [PRIMARY]
;

SET IDENTITY_INSERT dbo.DimProductPlan ON
;
INSERT INTO dbo.DimProductPlan (ProdPlanKey, ProdPlan_ID, ProdPlan_Name, Department_Name, Price, Source, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
VALUES (-1, '-1', 'Unknown', 'Unknown Department', -1, '', 'Y', '12/31/1899', '12/31/9999', 'N/A')
;
SET IDENTITY_INSERT dbo.DimProductPlan OFF
;



/* Drop table dbo.DimCustomerAccount */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'dbo.DimCustomerAccount') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE dbo.DimCustomerAccount 
;

/* Create table dbo.DimCustomerAccount */
CREATE TABLE dbo.DimCustomerAccount (
   [CustAcctKey]  int IDENTITY  NOT NULL
,  [Customer_ID] int NULL
,  [Account_ID] int NULL
,  [CustAcct_Email]  varchar(200)   NOT NULL
,  [CustAcct_FirstName]  varchar(50)   NOT NULL
,  [CustAcct_LastName]  varchar(50)   NOT NULL
,  [CustAcct_FullName]  varchar(100)   NOT NULL
,  [CustAcct_Address]  varchar(1000)   NULL
,  [CustAcct_City]  varchar(50)   NULL
,  [CustAcct_State]  char(2)   NULL
,  [CustAcct_Zip]  char(5)   NULL
,  [CustAcct_Source]  varchar(50)   NOT NULL
,  [RowIsCurrent]  nchar(1)   NOT NULL
,  [RowStartDate]  datetime  DEFAULT '01/01/1970'  NOT NULL
,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
,  [RowChangeReason]  nvarchar(200)    NULL
, CONSTRAINT [PK_dbo.DimCustomerAccount] PRIMARY KEY CLUSTERED 
( [CustAcctKey] )
) ON [PRIMARY]
;


SET IDENTITY_INSERT dbo.DimCustomerAccount ON
;
INSERT INTO dbo.DimCustomerAccount (CustAcctKey, Customer_ID, Account_ID, CustAcct_Email, CustAcct_FirstName, CustAcct_LastName, CustAcct_FullName, CustAcct_Address, CustAcct_City, CustAcct_State, CustAcct_Zip, CustAcct_Source, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
VALUES (-1, -1, -1, '-1', 'Unknown Customer', 'Unknown Customer', 'Unknown Customer', 'Unknown Address', 'Unknown City', '', '', '', 'Y', '12/31/1899', '12/31/9999', 'N/A')
;
SET IDENTITY_INSERT dbo.DimCustomerAccount OFF
;




;

/* Create table dbo.FactOrderDetails */
CREATE TABLE dbo.FactOrderDetails (
   [ProdPlanKey]  int  NOT NULL
,  [CustAcctKey]  int   NOT NULL
,  [Order_Date]  int   NOT NULL
,  [Ship_Date] int NULL
,  [Order_ID]  int   NOT NULL
,  [Shipper]  varchar(20)   NULL
,  [Order_Qty]  int   NOT NULL
,  [Total_Sales_Amount]  money   NOT NULL
,  [Count_Orders]  int   NOT NULL
,  [Count_Orders_Shipped]  int   NOT NULL
,  [Days_to_Ship]  int  NULL
) ON [PRIMARY]
;





/* Create table dbo.FactAccountBilling */
CREATE TABLE dbo.FactAccountBilling (
   [ProdPlanKey]  int    NOT NULL
,  [CustAcctKey]  int   NOT NULL
,  [Bill_Date]  int  NOT NULL
,  [Acct_ID]  int   NOT NULL
,  [Total_Billed_Amount]  money   NOT NULL
,  [Count_Billing]  int   NOT NULL
) ON [PRIMARY]
;


ALTER TABLE dbo.FactOrderDetails ADD CONSTRAINT
   FK_dbo_FactOrderDetails_ProdPlanKey FOREIGN KEY
   (
   ProdPlanKey
   ) REFERENCES DimProductPlan
   ( ProdPlanKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE dbo.FactOrderDetails ADD CONSTRAINT
   FK_dbo_FactOrderDetails_CustAcctKey FOREIGN KEY
   (
   CustAcctKey
   ) REFERENCES DimCustomerAccount
   ( CustAcctKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE dbo.FactOrderDetails ADD CONSTRAINT
   FK_dbo_FactOrderDetails_Order_Date FOREIGN KEY
   (
   Order_Date
   ) REFERENCES DimDate
   ( DateKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE dbo.FactAccountBilling ADD CONSTRAINT
   FK_dbo_FactAccountBilling_ProdPlanKey FOREIGN KEY
   (
   ProdPlanKey
   ) REFERENCES DimProductPlan
   ( ProdPlanKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE dbo.FactAccountBilling ADD CONSTRAINT
   FK_dbo_FactAccountBilling_CustAcctKey FOREIGN KEY
   (
   CustAcctKey
   ) REFERENCES DimCustomerAccount
   ( CustAcctKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE dbo.FactAccountBilling ADD CONSTRAINT
   FK_dbo_FactAccountBilling_Bill_Date FOREIGN KEY
   (
   Bill_Date
   ) REFERENCES DimDate
   ( DateKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
