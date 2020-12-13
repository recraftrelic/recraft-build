cd $1

git init
git remote add origin $2
git add .
git commit -m "initial commit"
git push -u origin master
