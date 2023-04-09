using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;

public class PlayButton : MonoBehaviour
{
    public VideoPlayer videoPlayer;

    public void PlayVideo()
    {
        videoPlayer.Play();
    }
}