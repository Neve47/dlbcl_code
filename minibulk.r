library(Seurat)

args <- commandArgs(T)
data <- readRDS(args[1])
data$label <- gsub(" ","_",paste(data$celltype, data$nearest_bt, data$distance_group, sep="#"))
ll <- unique(data$label)

minibulk <- as.data.frame(rownames(data))
colnames(minibulk) <- c("gene")
rownames(minibulk) <- minibulk$gene
for (i in ll){
tmp <- subset(data, label==i)
df <- as.matrix(tmp@assays$RNA@counts)
aa <- rowSums(df)
minibulk[,i] <- aa[rownames(minibulk)]
}

bulk <- minibulk[,2:ncol(minibulk)]
mb <- CreateSeuratObject(counts=minibulk)

saveRDS(mb,args[2])
