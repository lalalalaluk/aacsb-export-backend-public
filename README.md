
# 啟動DB start dev db
docker-compose -f docker-compose.dev.yml up db

# 啟動Django start django
docker-compose -f docker-compose.dev.yml up web