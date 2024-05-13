# Databricks notebook source
df = spark.read.options(**{"header":True}).csv("file:/Workspace/Repos/databricks215@gmail.com/DatabricksTests/data/test.csv")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMPORARY VIEW test
# MAGIC USING csv 
# MAGIC OPTIONS (
# MAGIC   path 'file:/Workspace/Repos/databricks215@gmail.com/DatabricksTests/data/test.csv',
# MAGIC   header true
# MAGIC );
# MAGIC
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   test
# MAGIC LIMIT
# MAGIC   10

# COMMAND ----------


