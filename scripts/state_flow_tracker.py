#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAICD 状态流跟踪器
Human-AI Interaction Contextual Dynamics Model
State Flow Tracker - 跨对话状态跟踪

作者：Jeason (理论创建者), 智联星核 (ZLXH)
版本：v1.0.0
许可：CC BY-NC-SA 4.0
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class StateFlowTracker:
    """状态流跟踪器"""
    
    def __init__(self, session_id: str, storage_path: str = "~/.openclaw/skills/haicd-state-engine/state_flow.json"):
        """
        初始化跟踪器
        
        Args:
            session_id: 会话 ID
            storage_path: 状态流存储路径
        """
        self.session_id = session_id
        self.storage_path = os.path.expanduser(storage_path)
        self.state_history = self._load_history()
    
    def _load_history(self) -> Dict:
        """加载历史状态流"""
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"sessions": {}}
    
    def _save_history(self):
        """保存历史状态流"""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.state_history, f, ensure_ascii=False, indent=2)
    
    def record_state(self, state_name: str, context: Dict):
        """
        记录状态
        
        Args:
            state_name: 状态名称
            context: 上下文信息
        """
        timestamp = datetime.now().isoformat()
        
        if self.session_id not in self.state_history["sessions"]:
            self.state_history["sessions"][self.session_id] = {
                "created": timestamp,
                "states": [],
                "current_state": None
            }
        
        session = self.state_history["sessions"][self.session_id]
        session["states"].append({
            "state": state_name,
            "timestamp": timestamp,
            "context": context
        })
        session["current_state"] = state_name
        session["last_updated"] = timestamp
        
        self._save_history()
    
    def get_current_state(self) -> Optional[str]:
        """获取当前状态"""
        if self.session_id in self.state_history["sessions"]:
            return self.state_history["sessions"][self.session_id].get("current_state")
        return None
    
    def get_state_history(self, limit: int = 10) -> List[Dict]:
        """
        获取状态历史
        
        Args:
            limit: 返回最近 N 条记录
        
        Returns:
            状态历史记录列表
        """
        if self.session_id not in self.state_history["sessions"]:
            return []
        
        states = self.state_history["sessions"][self.session_id]["states"]
        return states[-limit:]
    
    def detect_anomalies(self) -> Dict:
        """
        检测异常
        
        Returns:
            异常检测报告
        """
        if self.session_id not in self.state_history["sessions"]:
            return {"anomalies": []}
        
        states = self.state_history["sessions"][self.session_id]["states"]
        anomalies = []
        
        # 检测频繁切换
        if len(states) >= 5:
            recent_states = [s["state"] for s in states[-5:]]
            unique_states = len(set(recent_states))
            if unique_states >= 4:
                anomalies.append({
                    "type": "frequent_switch",
                    "description": "5 步内状态切换超过 3 次",
                    "severity": "warning"
                })
        
        # 检测停滞
        if len(states) >= 10:
            recent_states = [s["state"] for s in states[-10:]]
            if len(set(recent_states)) == 1:
                anomalies.append({
                    "type": "stagnation",
                    "description": "10 步未切换状态",
                    "severity": "info"
                })
        
        return {"anomalies": anomalies}
    
    def clear_session(self):
        """清除当前会话状态"""
        if self.session_id in self.state_history["sessions"]:
            del self.state_history["sessions"][self.session_id]
            self._save_history()


# 使用示例
if __name__ == "__main__":
    tracker = StateFlowTracker("test-session-001")
    
    # 记录状态
    tracker.record_state("顺应", {"scenario": "academic_research"})
    tracker.record_state("高风险创新", {"scenario": "innovation"})
    
    # 获取当前状态
    current = tracker.get_current_state()
    print(f"当前状态：{current}")
    
    # 获取历史
    history = tracker.get_state_history(limit=5)
    print(f"状态历史：{history}")
    
    # 检测异常
    anomalies = tracker.detect_anomalies()
    print(f"异常检测：{anomalies}")
