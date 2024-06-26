library(Matrix)
library(Seurat)
library(cowplot)
library(dplyr)
library(patchwork)
library(DoubletFinder)

args<-commandArgs(T)

data <- readRDS(args[1])
seu_obj <- CreateSeuratObject(data, project = "DLBCL")
seu_obj <- SCTransform(seu_obj)
seu_obj <- RunPCA(seu_obj)
seu_obj <- RunUMAP(seu_obj, dims = 1:30)

sweep.res.list_obj <- paramSweep(seu_obj, PCs = 1:30, sct = T)
sweep.stats_obj <- summarizeSweep(sweep.res.list_obj, GT = FALSE)
bcmvn_obj <- find.pK(sweep.stats_obj)

annotations <- seu_obj@meta.data$ClusteingResults
homotypic.prop <- modelHomotypic(annotations)
nExp_poi <- round(0.075*nrow(seu_obj@meta.data))
nExp_poi.adj <- round(nExp_poi*(1-homotypic.prop))

seu_obj <- doubletFinder(seu_obj, PCs = 1:30, pN = 0.25, pK = 0.09, nExp = nExp_poi.adj, reuse.pANN = FALSE, sct = T)

data <- seu_obj
colnames(data@meta.data) <- c("orig.ident","nCount_RNA","nFeature_RNA","nCount_SCT","nFeature_SCT","pANN","DF")
data <- RenameCells(data,new.names=paste(colnames(data),args[2],sep="_"))
data$item <- args[2]

data <- subset(data,DF=="Singlet")
saveRDS(data,args[3])

