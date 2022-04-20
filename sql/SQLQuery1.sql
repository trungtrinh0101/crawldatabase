USE BATDONGSAN
GO
IF OBJECT_ID('real_estate') IS NOT NULL
	DROP TABLE real_estate;
GO

CREATE TABLE real_estate(
	title			NVARCHAR(100) NOT NULL,
	price			NVARCHAR(100) NOT NULL,
	description		NVARCHAR(100) NOT NULL,
	distCity		NVARCHAR(100) NOT NULL,
	uptime			DATETIME NOT NULL ,
	productArea		NVARCHAR(100) NOT NULL,
	photoSample		VARBINARY NOT NULL
);
GO

SELECT * 
FROM real_estate