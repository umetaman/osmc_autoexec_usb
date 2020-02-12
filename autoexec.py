import xbmc
import glob

# USBドライブは/media以下にマウントされる
# ワイルドカードで/mediaにあるすべてのmp4の動画のパスを取得する

videoFiles = []
for videoFile in glob.iglob("/media/*/*.mp4")
    videoFiles.append(videoFile)

# プレイリストのオブジェクトを作る
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playList.clear()

# プレイリストに追加する
for videoFile in videoFiles:
    playList.add(url=videoFile)

# 再生する
xbmc.Player().play(playList)