Rows,Cols=len(matrix),len(matrix[0])
rowZero=False
for r in range(Rows):
  for c in range(Cols):
    if matrix[r][c]==0:
      if r>0:
        matrix[r][0]=0
      else:
        rowZero=True
for r in range(1,Rows):
  for c in range(1,Cols):
    if matrix[0][c]==0 or matrix[r][0]==0:
      matrix[r][c]=0
if matrix[0][0]==0:
  for r in range(Rows):
    matrix[r][0]=0
if rowZero:
  for c in range(Cols):
    matrix[0][c]=0
