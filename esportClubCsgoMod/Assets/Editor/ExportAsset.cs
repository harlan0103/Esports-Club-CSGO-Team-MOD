using UnityEngine;
using UnityEditor;
using System.Collections;
using System.IO;

public class ExportAsset : MonoBehaviour {

    /// <summary>  
    /// 将选中的预制分别打包  
    /// </summary>  
    [MenuItem("AssetBundle/Create AssetBundles")]
    static void CreateAssetBundle()
    {
        string targetPath = Application.dataPath + "/StreamingAssets/";

        if(Directory.Exists(targetPath))
        {
            Directory.Delete(targetPath, true);
        }
        Directory.CreateDirectory(targetPath);

        BuildPipeline.BuildAssetBundles(targetPath);

        DirectoryInfo dir = new DirectoryInfo(targetPath);
        foreach (var file in dir.GetFiles())
        {
            if(file.Extension == ".manifest" || file.Name == "StreamingAssets")
            {
                file.Delete();
            }
        }

        //刷新编辑器（不写的话要手动刷新,否则打包的资源不能及时在Project视图内显示）  
        AssetDatabase.Refresh();

        string dataPath = targetPath + "Data/";
        string imagePath = targetPath + "Image/";

        if (!Directory.Exists(dataPath))
        {
            Directory.CreateDirectory(dataPath);
        }
        if (!Directory.Exists(imagePath))
        {
            Directory.CreateDirectory(imagePath);
        }

        foreach (var file in dir.GetFiles())
        {
            if(file.Name.Contains("data"))
            {
                if (File.Exists(dataPath + file.Name))
                {
                    file.CopyTo(dataPath + file.Name, true);
                    file.Delete();
                }
                else
                    file.MoveTo(dataPath + file.Name);
            }
            else
            {
                if (File.Exists(imagePath + file.Name))
                {
                    file.CopyTo(imagePath + file.Name, true);
                    file.Delete();
                }
                else
                    file.MoveTo(imagePath + file.Name);
            }
        }

        Debug.Log("Export Complete.");

        System.Diagnostics.Process.Start(targetPath);

        AssetDatabase.Refresh();

    }
}
